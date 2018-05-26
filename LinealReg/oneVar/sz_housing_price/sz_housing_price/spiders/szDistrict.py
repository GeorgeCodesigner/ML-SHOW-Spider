class szDistrict(object):
    def __init__(self):
        pass
    def getDistrict(self):
        District = {
            # 龙岗区
            'house-a090-b0352/':'buji',
            'house-a090-b0354/':'lgzxc',
            'house-a090-b0351/':'bantian',
            'house-a090-b0353/':'henggang',
            'house-a090-b02087/':'pinghu',
            'house-a090-b02089/':'pingdi',
            # 龙华区
            'house-a013080-b0350/':'longhua',
            'house-a013080-b014334/':'dalang',
            'house-a013080-b014333/':'minzhi',
            'house-a013080-b02094/':'guanlan',
            # 宝安区
            'house-a089-b02092/':'xixiang',
            'house-a089-b0349/':'bazxq',
            'house-a089-b02093/':'xinan',
            'house-a089-b02097/':'fuyong',
            'house-a089-b02096/':'songgang',
            'house-a089-b02098/':'shajing',
            'house-a089-b02095/':'shiyan',
            # 南山区
            'house-a087-b0344/':'qianhai',
            'house-a087-b0346/':'shekou',
            'house-a087-b0342/':'nantou',
            'house-a087-b0340/':'kejiyuan',
            'house-a087-b04800/':'nszxq',
            'house-a087-b0339/':'huaqiaocheng',
            'house-a087-b0343/':'nanyou',
            'house-a087-b0345/':'houhai',
            'house-a087-b0341/':'xili',
            # 福田区
            'house-a085-b0320/':'huanggang',
            'house-a085-b0323/':'jingtian',
            'house-a085-b0325/':'meilin',
            'house-a085-b0318/':'huaqiang',
            'house-a085-b0324/':'xiangmihu',
            'house-a085-b0322/':'ftzxq',
            'house-a085-b0317/':'shangbu',
            'house-a085-b0321/':'xinzhou',
            'house-a085-b02084/':'shixia',
            'house-a085-b0319/':'lianhua',
            'house-a085-b02086/':'nkzx',
            'house-a085-b0327/':'shangxiasha',
            'house-a085-b0316/':'bagualing',
            'house-a085-b04647/':'zhuzilin',
            'house-a085-b02085/':'baoshuiqu',
            'house-a085-b0326/':'chegongmiao',
            'house-a085-b02083/':'bijiashan',
            # 罗湖区
            'house-a086-b0331/':'buxin',
            'house-a086-b0328/':'liantang',
            'house-a086-b0329/':'huangbeiling',
            'house-a086-b0330/':'shuiku',
            'house-a086-b0332/':'cuizhu',
            'house-a086-b0336/':'caiwuwei',
            'house-a086-b0335/':'dongmen',
            'house-a086-b0334/':'renminnan',
            'house-a086-b0333/':'sungang',
            'house-a086-b04648/':'honghu',
            'house-a086-b02082/':'nigang',
            'house-a086-b0337/':'baoannan',
            'house-a086-b0338/':'yinhu',
            # 坪山区
            'house-a013081-b02088/':'pingshan',
            'house-a013081-b010054/':'kengzi',
            # 光明新区
            'house-a013079-b010047/':'gongming',
            'house-a013079-b02099/':'guangming',
            # 盐田区
            'house-a088-b0348/':'shatoujiao',
            'house-a088-b0347/':'meisha',
            'house-a088-b010040/':'yantiangang',
            # 大鹏新区
            'house-a013082-b010056/':'dapeng',
            # 'house-a013082-b02091/':'nanao', # 只有4条数据且不符合线性，不需要爬取
            'house-a013082-b04214/':'kuichong'
        }
        return District