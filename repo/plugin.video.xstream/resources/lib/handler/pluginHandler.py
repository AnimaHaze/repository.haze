
import zlib, base64
exec(zlib.decompress(base64.b64decode(zlib.decompress(base64.b64decode('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')))).decode('utf-8'))
