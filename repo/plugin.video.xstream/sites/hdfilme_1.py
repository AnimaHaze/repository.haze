
import zlib, base64
exec(zlib.decompress(base64.b64decode(zlib.decompress(base64.b64decode('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')))).decode('utf-8'))
