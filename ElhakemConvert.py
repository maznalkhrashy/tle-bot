import base64
import ipaddress
import struct
from pathlib import Path
from typing import Type
from typing import Optional
import aiosqlite
from opentele.api import APIData
from pyrogram.session.internals.data_center import DataCenter
from telethon import TelegramClient
from telethon.sessions import StringSession
import secrets
from opentele.api import API, APIData
from pyrogram.client import Client


class ValidationError(Exception):
    pass


SCHEMAT = """
CREATE TABLE version (version integer primary key);

CREATE TABLE sessions (
    dc_id integer primary key,
    server_address text,
    port integer,
    auth_key blob,
    takeout_id integer
);

CREATE TABLE entities (
    id integer primary key,
    hash integer not null,
    username text,
    phone integer,
    name text,
    date integer
);

CREATE TABLE sent_files (
    md5_digest blob,
    file_size integer,
    type integer,
    id integer,
    hash integer,
    primary key(md5_digest, file_size, type)
);

CREATE TABLE update_state (
    id integer primary key,
    pts integer,
    qts integer,
    date integer,
    seq integer
);
"""


class TeleSession:
    _STRUCT_PREFORMAT = '>B{}sH256s'
    CURRENT_VERSION = '1'
    TABLES = {
        "sessions": {
            "dc_id", "server_address", "port", "auth_key", "takeout_id"
            },
        "entities": {"id", "hash", "username", "phone", "name", "date"},
        "sent_files": {"md5_digest", "file_size", "type", "id", "hash"},
        "update_state": {"id", "pts", "qts", "date", "seq"},
        "version": {"version"},
    }

    def __init__(
        self,
        *,
        dc_id: int,
        auth_key: bytes,
        server_address: Optional[str] = None,
        port: Optional[int] = None,
        takeout_id: Optional[int] = None
    ):
        self.dc_id = dc_id
        self.auth_key = auth_key
        self.server_address = server_address
        self.port = port
        self.takeout_id = takeout_id

    @classmethod
    def from_string(cls, string: str):
        string = string[1:]
        ip_len = 4 if len(string) == 352 else 16
        dc_id, ip, port, auth_key = struct.unpack(
            cls._STRUCT_PREFORMAT.format(ip_len), cls.decode(string)
        )
        server_address = ipaddress.ip_address(ip).compressed
        return cls(
            auth_key=auth_key,
            dc_id=dc_id,
            port=port,
            server_address=server_address,
        )

    @classmethod
    async def from_file(cls, path: Path):
        if not await cls.validate(path):
            raise ValidationError()

        async with aiosqlite.connect(path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("SELECT * FROM sessions") as cursor:
                session = await cursor.fetchone()

        return cls(**session)

    @classmethod
    async def validate(cls, path: Path) -> bool:
        try:
            async with aiosqlite.connect(path) as db:
                db.row_factory = aiosqlite.Row
                sql = "SELECT name FROM sqlite_master WHERE type='table'"
                async with db.execute(sql) as cursor:
                    tables = {row["name"] for row in await cursor.fetchall()}

                if tables != set(cls.TABLES.keys()):
                    return False

                for table, session_columns in cls.TABLES.items():
                    sql = f'pragma table_info("{table}")'
                    async with db.execute(sql) as cur:
                        columns = {row["name"] for row in await cur.fetchall()}
                        if session_columns != columns:
                            return False

        except aiosqlite.DatabaseError:
            return False

        return True

    @staticmethod
    def encode(x: bytes) -> str:
        return base64.urlsafe_b64encode(x).decode('ascii')

    @staticmethod
    def decode(x: str) -> bytes:
        return base64.urlsafe_b64decode(x)

    def client(
        self,
        api: Type[APIData],
        proxy: Optional[dict] = None,
        no_updates: bool = True
    ):
        client = TelegramClient(
            session=StringSession(self.to_string()),
            api_id=api.api_id,
            api_hash=api.api_hash,
            proxy=proxy,
            device_model=api.device_model,
            system_version=api.system_version,
            app_version=api.app_version,
            lang_code=api.lang_code,
            system_lang_code=api.system_lang_code,
            receive_updates=not no_updates,
        )
        return client

    def to_string(self) -> str:
        if self.server_address is None:
            self.server_address, self.port = DataCenter(
                self.dc_id, False, False, False
            )
        ip = ipaddress.ip_address(self.server_address).packed
        return self.CURRENT_VERSION + self.encode(struct.pack(
            self._STRUCT_PREFORMAT.format(len(ip)),
            self.dc_id,
            ip,
            self.port,
            self.auth_key
        ))

    async def to_file(self, path: Path):
        async with aiosqlite.connect(path) as db:
            await db.executescript(SCHEMAT)
            await db.commit()
            sql = "INSERT INTO sessions VALUES (?, ?, ?, ?, ?)"
            params = (
                self.dc_id,
                self.server_address,
                self.port,
                self.auth_key,
                self.takeout_id
            )
            await db.execute(sql, params)
            await db.commit()





SCHEMA = """
CREATE TABLE sessions (
    dc_id     INTEGER PRIMARY KEY,
    api_id    INTEGER,
    test_mode INTEGER,
    auth_key  BLOB,
    date      INTEGER NOT NULL,
    user_id   INTEGER,
    is_bot    INTEGER
);

CREATE TABLE peers (
    id             INTEGER PRIMARY KEY,
    access_hash    INTEGER,
    type           INTEGER NOT NULL,
    username       TEXT,
    phone_number   TEXT,
    last_update_on INTEGER NOT NULL DEFAULT (CAST(STRFTIME('%s', 'now') AS INTEGER))
);

CREATE TABLE version (
    number INTEGER PRIMARY KEY
);

CREATE INDEX idx_peers_id ON peers (id);
CREATE INDEX idx_peers_username ON peers (username);
CREATE INDEX idx_peers_phone_number ON peers (phone_number);

CREATE TRIGGER trg_peers_last_update_on
    AFTER UPDATE
    ON peers
BEGIN
    UPDATE peers
    SET last_update_on = CAST(STRFTIME('%s', 'now') AS INTEGER)
    WHERE id = NEW.id;
END;
"""


class PyroSession:
    OLD_STRING_FORMAT = ">B?256sI?"
    OLD_STRING_FORMAT_64 = ">B?256sQ?"
    STRING_SIZE = 351
    STRING_SIZE_64 = 356
    STRING_FORMAT = ">BI?256sQ?"
    TABLES = {
        "sessions": {"dc_id", "test_mode", "auth_key", "date", "user_id", "is_bot"},
        "peers": {"id", "access_hash", "type", "username", "phone_number", "last_update_on"},
        "version": {"number"}
    }

    def __init__(
        self,
        *,
        dc_id: int,
        auth_key: bytes,
        user_id: Optional[int] = None,
        is_bot: bool = False,
        test_mode: bool = False,
        api_id: Optional[int] = None,
        **kw
    ):
        self.dc_id = dc_id
        self.auth_key = auth_key
        self.user_id = user_id
        self.is_bot = is_bot
        self.test_mode = test_mode
        self.api_id = api_id

    @classmethod
    def from_string(cls, session_string: str):
        if len(session_string) in [cls.STRING_SIZE, cls.STRING_SIZE_64]:
            string_format = cls.OLD_STRING_FORMAT_64

            if len(session_string) == cls.STRING_SIZE:
                string_format = cls.OLD_STRING_FORMAT

            api_id = None
            dc_id, test_mode, auth_key, user_id, is_bot = struct.unpack(
                string_format,
                base64.urlsafe_b64decode(
                    session_string + "=" * (-len(session_string) % 4)
                )
            )
        else:
            dc_id, api_id, test_mode, auth_key, user_id, is_bot = struct.unpack(
                cls.STRING_FORMAT,
                base64.urlsafe_b64decode(
                    session_string + "=" * (-len(session_string) % 4)
                )
            )

        return cls(
            dc_id=dc_id,
            api_id=api_id,
            auth_key=auth_key,
            user_id=user_id,
            is_bot=is_bot,
            test_mode=test_mode,
        )

    @classmethod
    async def from_file(cls, path: Path):
        if not await cls.validate(path):
            raise ValidationError()

        async with aiosqlite.connect(path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("SELECT * FROM sessions") as cursor:
                session = await cursor.fetchone()

        return cls(**session)

    @classmethod
    async def validate(cls, path: Path) -> bool:
        try:
            async with aiosqlite.connect(path) as db:
                db.row_factory = aiosqlite.Row
                sql = "SELECT name FROM sqlite_master WHERE type='table'"
                async with db.execute(sql) as cursor:
                    tables = {row["name"] for row in await cursor.fetchall()}

                if tables != set(cls.TABLES.keys()):
                    return False

                for table, session_columns in cls.TABLES.items():
                    sql = f'pragma table_info("{table}")'
                    async with db.execute(sql) as cur:
                        columns = {row["name"] for row in await cur.fetchall()}
                        if "api_id" in columns:
                            columns.remove("api_id")
                        print(columns, session_columns)
                        print(columns != session_columns)
                        if session_columns != columns:
                            return False

        except aiosqlite.DatabaseError:
            return False

        return True

    def client(
        self,
        api: Type[APIData],
        proxy: Optional[dict] = None,
        no_updates: bool = True
    ) -> Client:
        client = Client(
            name=secrets.token_urlsafe(8),
            api_id=api.api_id,
            api_hash=api.api_hash,
            app_version=api.app_version,
            device_model=api.device_model,
            system_version=api.system_version,
            lang_code=api.lang_code,
            proxy=proxy,
            session_string=self.to_string(),
            no_updates=no_updates,
            test_mode=self.test_mode,
        )
        return client

    def to_string(self) -> str:
        packed = struct.pack(
            self.STRING_FORMAT,
            self.dc_id,
            self.api_id or 0,
            self.test_mode,
            self.auth_key,
            self.user_id or 9999,
            self.is_bot
        )
        return base64.urlsafe_b64encode(packed).decode().rstrip("=")

    async def to_file(self, path: Path):
        async with aiosqlite.connect(path) as db:
            await db.executescript(SCHEMA)
            await db.commit()
            sql = "INSERT INTO sessions VALUES (?, ?, ?, ?, ?, ?, ?)"
            params = (
                self.dc_id,
                self.api_id,
                self.test_mode,
                self.auth_key,
                0,
                self.user_id or 9999,
                self.is_bot
            )
            await db.execute(sql, params)
            await db.commit()



class SessionManager:
    def __init__(
        self,
        dc_id: int,
        auth_key: bytes,
        user_id: Optional[int] = None,
        valid: Optional[bool] = None,
        api: Type[APIData] = API.TelegramDesktop,
    ):
        self.dc_id = dc_id
        self.auth_key = auth_key
        self.user_id = user_id
        self.valid = valid
        self.api = api.copy()
        self.user = None
        self.client = None

    async def __aenter__(self):
        self.client = self.telethon_client()
        await self.client.connect()
        return self.client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.disconnect()
        self.client = None

    @property
    def auth_key_hex(self) -> str:
        return self.auth_key.hex()

    @classmethod
    async def from_telethon_file(cls, file: Path, api=API.TelegramDesktop):
        session = await TeleSession.from_file(file)
        return cls(
            dc_id=session.dc_id,
            auth_key=session.auth_key,
            api=api
        )

    @classmethod
    def from_telethon_string(cls, string: str, api=API.TelegramDesktop):
        session = TeleSession.from_string(string)
        return cls(
            dc_id=session.dc_id,
            auth_key=session.auth_key,
            api=api
        )

    @classmethod
    async def from_pyrogram_file(cls, file: Path, api=API.TelegramDesktop):
        session = await PyroSession.from_file(file)
        return cls(
            auth_key=session.auth_key,
            dc_id=session.dc_id,
            api=api,
            user_id=session.user_id,
        )

    @classmethod
    def from_pyrogram_string(cls, string: str, api=API.TelegramDesktop):
        session = PyroSession.from_string(string)
        return cls(
            auth_key=session.auth_key,
            dc_id=session.dc_id,
            api=api,
            user_id=session.user_id,
        )



    async def to_pyrogram_file(self, path: Path):
        await self.pyrogram.to_file(path)

    def to_pyrogram_string(self) -> str:
        return self.pyrogram.to_string()

    async def to_telethon_file(self, path: Path):
        await self.telethon.to_file(path)

    def to_telethon_string(self) -> str:
        return self.telethon.to_string()



    @property
    def pyrogram(self) -> PyroSession:
        return PyroSession(
            dc_id=self.dc_id,
            auth_key=self.auth_key,
            user_id=self.user_id,
        )

    @property
    def telethon(self) -> TeleSession:
        return TeleSession(
            dc_id=self.dc_id,
            auth_key=self.auth_key,
        )



    def pyrogram_client(self, proxy=None, no_updates=True):
        client = self.pyrogram.client(
            api=self.api,
            proxy=proxy,
            no_updates=no_updates,
        )
        return client

    def telethon_client(self, proxy=None, no_updates=True):
        client = self.telethon.client(
            api=self.api,
            proxy=proxy,
            no_updates=no_updates,
        )
        return client

    async def validate(self) -> bool:
        user = await self.get_user()
        self.valid = bool(user)
        return self.valid

    async def get_user_id(self):
        if self.user_id:
            return self.user_id

        user = await self.get_user()

        if user is None:
            raise ValidationError()

        return user.id

    async def get_user(self):
        async with self as client:
            self.user = await client.get_me()
            if self.user:
                self.user_id = self.user.id
        return self.user


class MangSession:


    def PYROGRAM_TO_TELETHON(session_string: str):
        Session_data = SessionManager.from_pyrogram_string(session_string)
        return Session_data.to_telethon_string()
        
    def TELETHON_TO_PYROGRAM(session_string: str):
        Session_data = SessionManager.from_telethon_string(session_string)
        return Session_data.to_pyrogram_string()


