class Life360Error(Exception):
    """Base class for SL exceptions"""
    pass


class LoginError(SLError):
    """Invalid api credentials"""
    pass

class APIQoutaError(SLError):
    """API Qouta exceeded"""
    pass
