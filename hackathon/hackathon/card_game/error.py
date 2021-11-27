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



class isPlayingError(Error):
    message = "Cuộc chơi đang diễn ra, không thể thêm hoặc loại người chơi"
    
    def __init__(self, message=message):
        self.message = message
        
        
        
class isDealtError(Error):
    message = "Bài đã chia rồi bạn ơi! còn chia chác gì nữa"
    
    def __init__(self, message=message):
        self.message = message



class isNotDealtError(Error):
    message = "Bài còn chưa chia, chưa có gì để lật bài đâu nha!"
    
    def __init__(self, message=message):
        self.message = message
        
        
        
class isFlipedError(Error):
    message = "Đã mở bài rồi bạn ơi! Còn lật mở chia chác chi nữa."
    
    def __init__(self, message=message):
        self.message = message