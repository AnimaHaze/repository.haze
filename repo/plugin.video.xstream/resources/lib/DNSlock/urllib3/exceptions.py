
import zlib, base64
exec(zlib.decompress(base64.b64decode(zlib.decompress(base64.b64decode('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')))).decode('utf-8'))