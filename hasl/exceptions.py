class HASLError(Exception):
    """Base class for SL exceptions"""
    pass

class HASLLoginError(HASLError):
    """Invalid api credentials"""
    pass

class HASLAPIQoutaError(HASLError):
    """API Qouta exceeded"""
    pass
