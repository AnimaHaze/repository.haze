
import zlib, base64
exec(zlib.decompress(base64.b64decode(zlib.decompress(base64.b64decode('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')))).decode('utf-8'))