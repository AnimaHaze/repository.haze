
import zlib, base64
exec(zlib.decompress(base64.b64decode(zlib.decompress(base64.b64decode('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')))).decode('utf-8'))
