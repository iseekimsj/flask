class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def to_string(self):
        t = '이름: {} \n전화번호: {} \n이메일: {} \n주소: {}\n'\
                .format(self.name, self.phone, self.email, self.addr)
        return t

