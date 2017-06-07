class Device:
    """Class for communicating with an I2C device.

    Allows reading and writing 8-bit, 16-bit, and byte array values to
    registers on the device."""

    def __init__(self, address, i2c):
        """Create an instance of the I2C device at the specified address using
        the specified I2C interface object."""
        self._address = address
        self._i2c = i2c

    def writeRaw8(self, value):
        """Write an 8-bit value on the bus (without register)."""
        value = value & 0xFF
        self._i2c.writeto(self._address, value.to_bytes(1))

    def write8(self, register, value):
        """Write an 8-bit value to the specified register."""
        value = value & 0xFF
        self._i2c.writeto_mem(self._address, register, value.to_bytes(1))

    def write16(self, register, value):
        """Write a 16-bit value to the specified register."""
        value = value & 0xFFFF
        self.i2c.writeto_mem(self._address, register, value)

    def readRaw8(self):
        """Read an 8-bit value on the bus (without register)."""
        return int.from_bytes(self._i2c.readfrom(self._address, 1)) & 0xFF

    def readU8(self, register):
        """Read an unsigned byte from the specified register."""
        return int.from_bytes(
            self._i2c.readfrom_mem(self._address, register, 1)) & 0xFF

    def readS8(self, register):
        """Read a signed byte from the specified register."""
        result = self.readU8(register)
        if result > 127:
            result -= 256
        return result

    def readU16(self, register, little_endian=True):
        """Read an unsigned 16-bit value from the specified register, with the
        specified endianness (default little endian, or least significant byte
        first)."""
        result = int.from_bytes(self._i2c.readfrom_mem(self._address, register, 2)) & 0xFFFF
        if not little_endian:
            result = ((result << 8) & 0xFF00) + (result >> 8)
        return result

    def readS16(self, register, little_endian=True):
        """Read a signed 16-bit value from the specified register, with the
        specified endianness (default little endian, or least significant byte
        first)."""
        result = self.readU16(register, little_endian)
        if result > 32767:
            result -= 65536
        return result

    def readU16LE(self, register):
        """Read an unsigned 16-bit value from the specified register, in little
        endian byte order."""
        return self.readU16(register, little_endian=True)

    def readU16BE(self, register):
        """Read an unsigned 16-bit value from the specified register, in big
        endian byte order."""
        return self.readU16(register, little_endian=False)

    def readS16LE(self, register):
        """Read a signed 16-bit value from the specified register, in little
        endian byte order."""
        return self.readS16(register, little_endian=True)

    def readS16BE(self, register):
        """Read a signed 16-bit value from the specified register, in big
        endian byte order."""
        return self.readS16(register, little_endian=False)
