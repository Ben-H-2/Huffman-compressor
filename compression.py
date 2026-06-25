import gzip

def format_bits_to_bytes(bit_count):
    if bit_count>8:
        byte_count = bit_count//8
        if byte_count > 1000:
            kilobyte_count = byte_count/1000
            if kilobyte_count > 1000:
                megabyte_count = kilobyte_count/1000
                return f"{str(round(megabyte_count,1)) + " MB"}"
            else:
                return f"{str(round(kilobyte_count,1)) + " KB"}"
        else:
            return f"{str(byte_count) + " bytes"}"
    else:
        return f"{str(bit_count) + " bits"}"
    

def gzip_compression_size_bits(text):
    text_bytes = text.encode("utf-8")
    compressed_bytes = gzip.compress(text_bytes)
    return len(compressed_bytes*8)

