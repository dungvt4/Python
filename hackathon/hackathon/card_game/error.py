class Error(Exception):
    '''Base class cho game error'''
    pass

class MaximumPlayersError(Error):
    message = "Đã quá số lượng người chơi, không thể thêm được nữa"
    
    def __init__(self, message=message):
        self.message = message

class MinimumPlayersError(Error):
    message = "Số lượng người chơi tối thiếu, không thể loại đc nữa"
    
    def __init__(self, message=message):
        self.message = message

class MenuOptionError(Error):
    message = "Bạn cần nhập đúng theo menu hướng dẫn"
    
    def __init__(self, message=message):
        self.message = message 
        
class NotIntegerError(Error):
    message = "Bạn phải nhập số nguyên dương"
    
    def __init__(self, message=message):
        self.message = message 
        
class NotFoundPlayerError(Error):
    message = "Không tìm thấy ID người dùng, không thể xóa"
    
    def __init__(self, message=message):
        self.message = message