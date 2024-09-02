class Tv:

    def __init__(self,tv_id,tv_name):
        self.tv_id = tv_id
        self.tv_name = tv_name
        self.connect_remotecontrol = 0
        

    def connect(self,tv):
        tv.connect_remotecontrol = +1
    


tv1 = Tv("20110011","LG스마트55인치")
tv2 = Tv("20240001","삼성UHD200인치")


print(f"tv1 : id:{tv1.tv_id}, tv1 : name {tv1.tv_name}")
tv1.connect(tv1)
print("tv1에 리모컨 동기화 되었습니다.")
print(f"{tv1.connect_remotecontrol}")