
import zlib, base64
exec(zlib.decompress(base64.b64decode(zlib.decompress(base64.b64decode('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')))).decode('utf-8'))