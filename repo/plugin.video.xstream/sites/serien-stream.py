
import zlib, base64
exec(zlib.decompress(base64.b64decode(zlib.decompress(base64.b64decode('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')))).decode('utf-8'))