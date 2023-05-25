#!/usr/bin/python env
# -*- coding: utf-8 -*-
import sys,os,json
sys.path.append("lib")
from PublicConfig import Config
from TxCloudCvmApi import TxCloudCvmApiRequest


class TxColudCvmOper():
     def __init__(self,region=None):
         self.logo = "è…¾è®¯äº‘"
         self.Region = region
         self.initTxConfig = Config()
         self.secretId = self.initTxConfig.GetConfig()['PublicParams']['secretId']
         self.secretKey = self.initTxConfig.GetConfig()['PublicParams']['secretKey']
         self.initTxCvmApi = TxCloudCvmApiRequest(
                            secretId=self.secretId,
                            secretKey=self.secretKey,
                            region=self.Region
         )

     def GetCvmImageList(self):
         """
         èŽ·å–é•œåƒåˆ—è¡¨
         """
         RequestResult = self.initTxCvmApi.GetImasgeListRequest()
         if RequestResult['status'] == True:
            for ImagesInfo in RequestResult['message']:
                print(f"""
                       é•œåƒID    : {ImagesInfo.ImageId}
                       é•œåƒOS    : {ImagesInfo.OsName}
                       é•œåƒç±»åž‹  : {ImagesInfo.ImageType}
                       é•œåƒåå­—  : {ImagesInfo.ImageName}
                       é•œåƒæº    : {ImagesInfo.ImageSource}
                """)
         else:
             print(f"""
                  èŽ·å–{self.logo}é•œåƒåˆ—è¡¨å¤±è´¥
                           çŠ¶æ€: {RequestResult['status']}
                           å¼‚å¸¸: {RequestResult['message']}
                  """)

     def GetInstanceList(self):
         """
         æŸ¥çœ‹å®žä¾‹ä¿¡æ¯
         """
         RequestResult = self.initTxCvmApi.GetInstanceIdListRequest()
         if RequestResult['status'] == True:
            for InstanceInfo in RequestResult['message']:
                print(f"""
                      æœºå™¨ä½ç½®   : {InstanceInfo.Placement.Zone}
                      å®žä¾‹ID     : {InstanceInfo.InstanceId}
                      å®žä¾‹ç±»åž‹   : {InstanceInfo.InstanceType} 
                      å®žä¾‹å¤‡æ³¨   : {InstanceInfo.InstanceName}
                      å®žä¾‹å†…å­˜   : {InstanceInfo.Memory}
                      å®žä¾‹CPU    : {InstanceInfo.CPU}
                      ç£ç›˜å¤§å°   : {InstanceInfo.SystemDisk.DiskSize}
                      å®žä¾‹å†…ç½‘   : {InstanceInfo.PrivateIpAddresses}
                      å®žä¾‹å…¬ç½‘   : {InstanceInfo.PublicIpAddresses}
                      è®¡è´¹ç±»åž‹   : {InstanceInfo.InstanceChargeType} PS: POSTPAID_BY_HOURæŒ‰å°æ—¶åŽä»˜è´¹ PREPAIDé¢„ä»˜è´¹ï¼Œå³åŒ…å¹´åŒ…æœˆ é»˜è®¤å€¼POSTPAID_BY_HOUR
                      é•œåƒID     : {InstanceInfo.ImageId}   
                      åˆ›å»ºæ—¥æœŸ   : {InstanceInfo.CreatedTime}
                      è¿‡æœŸæ—¶é—´   : {InstanceInfo.ExpiredTime}   
                      å®žä¾‹OS     : {InstanceInfo.OsName}
                      å®žä¾‹çŠ¶æ€   : {InstanceInfo.InstanceState}
                      å®žä¾‹ç”¨æˆ·   : {InstanceInfo.DefaultLoginUser}
                      å®žä¾‹ç«¯å£   : {InstanceInfo.DefaultLoginPort}
                      è®¸å¯ç±»åž‹   : {InstanceInfo.LicenseType}""")
         else:
             print(f"""
                  èŽ·å–{self.logo}å®žä¾‹åˆ—è¡¨å¤±è´¥
                           çŠ¶æ€: {RequestResult['status']}
                           å¼‚å¸¸: {RequestResult['message']}
             """)


     def CreateInstance(self):
         """
         InstanceChargeType    å®žä¾‹è®¡è´¹ç±»åž‹ PREPAIDï¼šé¢„ä»˜è´¹ï¼Œå³åŒ…å¹´åŒ…æœˆ POSTPAID_BY_HOURï¼šæŒ‰å°æ—¶åŽä»˜è´¹ é»˜è®¤å€¼ï¼šPOSTPAID_BY_HOURã€‚
         Placement	           Placement objectå®žä¾‹æ‰€åœ¨çš„ä½ç½®ã€‚é€šè¿‡è¯¥å‚æ•°å¯ä»¥æŒ‡å®šå®žä¾‹æ‰€å±žå¯ç”¨åŒºï¼Œæ‰€å±žé¡¹ç›®ç­‰å±žæ€§ã€‚
         ImageId               æŒ‡å®šæœ‰æ•ˆçš„é•œåƒ IDï¼Œæ ¼å¼å½¢å¦‚img-xxxã€‚é•œåƒç±»åž‹åˆ†ä¸ºå››ç§ï¼šå…¬å…±é•œåƒ è‡ªå®šä¹‰é•œåƒ å…±äº«é•œåƒ æœåŠ¡å¸‚åœºé•œåƒ
         DisableApiTermination è¡¨ç¤ºå¼€å¯å®žä¾‹ä¿æŠ¤ï¼Œä¸å…è®¸é€šè¿‡apiæŽ¥å£åˆ é™¤å®žä¾‹ FALSEï¼šè¡¨ç¤ºå…³é—­å®žä¾‹ä¿æŠ¤ï¼Œå…è®¸é€šè¿‡apiæŽ¥å£åˆ é™¤å®žä¾‹ é»˜è®¤å–å€¼ï¼šFALSE
         ç£ç›˜é€‰æ‹©SystemDiskå­—æ®µ
             LOCAL_BASICï¼šæœ¬åœ°ç¡¬ç›˜
             LOCAL_SSDï¼šæœ¬åœ°SSDç¡¬ç›˜
             CLOUD_BASICï¼šæ™®é€šäº‘ç¡¬ç›˜
             CLOUD_SSDï¼šSSDäº‘ç¡¬ç›˜
             CLOUD_PREMIUMï¼šé«˜æ€§èƒ½äº‘ç¡¬ç›˜
             CLOUD_BSSDï¼šé€šç”¨æ€§SSDäº‘ç¡¬ç›˜
         è‡ªåŠ¨ç»­è´¹æ ‡è¯†ã€‚å–å€¼èŒƒå›´ï¼š
             NOTIFY_AND_AUTO_RENEWï¼šé€šçŸ¥è¿‡æœŸä¸”è‡ªåŠ¨ç»­è´¹
             NOTIFY_AND_MANUAL_RENEWï¼šé€šçŸ¥è¿‡æœŸä¸è‡ªåŠ¨ç»­è´¹
             DISABLE_NOTIFY_AND_MANUAL_RENEWï¼šä¸é€šçŸ¥è¿‡æœŸä¸è‡ªåŠ¨ç»­
         åˆ›å»ºwindowså®žä¾‹
             img-mmy6qctz  é•œåƒID
             S1.LARGE4     å®žä¾‹è§„æ ¼
         åˆ›å»ºcentoså®žä¾‹
             img-25szkc8t
             S6.MEDIUM4
         ç½‘ç»œé€‰æ‹©InternetAccessibleå­—æ®µ
            Instance
             ç½‘ç»œè®¡è´¹ç±»åž‹ã€‚å–å€¼èŒƒå›´ï¼š
             BANDWIDTH_PREPAIDï¼šé¢„ä»˜è´¹æŒ‰å¸¦å®½ç»“ç®—
             TRAFFIC_POSTPAID_BY_HOURï¼šæµé‡æŒ‰å°æ—¶åŽä»˜è´¹
             BANDWIDTH_POSTPAID_BY_HOURï¼šå¸¦å®½æŒ‰å°æ—¶åŽä»˜è´¹
             BANDWIDTH_PACKAGEï¼šå¸¦å®½åŒ…ç”¨æˆ·
             é»˜è®¤å–å€¼ï¼šéžå¸¦å®½åŒ…ç”¨æˆ·é»˜è®¤ä¸Žå­æœºä»˜è´¹ç±»åž‹ä¿æŒä¸€è‡´ã€‚
            InternetMaxBandwidthOut å…¬ç½‘å‡ºå¸¦å®½ä¸Šé™ï¼Œå•ä½ï¼šMbpsã€‚é»˜è®¤å€¼ï¼š0Mbps
            PublicIpAssigned
             æ˜¯å¦åˆ†é…å…¬ç½‘IPã€‚å–å€¼èŒƒå›´ï¼š
             TRUEï¼šè¡¨ç¤ºåˆ†é…å…¬ç½‘IP
              FALSEï¼šè¡¨ç¤ºä¸åˆ†é…å…¬ç½‘IP
            BandwidthPackageId	å¸¦å®½åŒ…IDã€‚å¯é€šè¿‡DescribeBandwidthPackagesæŽ¥å£è¿”å›žå€¼ä¸­çš„BandwidthPackageIdèŽ·å–
            å®žä¾‹è®¡è´¹ç±»åž‹ã€‚
              PREPAIDï¼šé¢„ä»˜è´¹ï¼Œå³åŒ…å¹´åŒ…æœˆ
              POSTPAID_BY_HOURï¼šæŒ‰å°æ—¶åŽä»˜è´¹
              CDHPAIDï¼šç‹¬äº«å­æœºï¼ˆåŸºäºŽä¸“ç”¨å®¿ä¸»æœºåˆ›å»ºï¼Œå®¿ä¸»æœºéƒ¨åˆ†çš„èµ„æºä¸æ”¶è´¹ï¼‰
              SPOTPAIDï¼šç«žä»·ä»˜è´¹
              CDCPAIDï¼šä¸“ç”¨é›†ç¾¤ä»˜è´¹
              é»˜è®¤å€¼ï¼šPOSTPAID_BY_HOURã€‚
         """
         params = {
             "ImageId":  "img-mmy6qctz",  # CentOS 7.6 64ä½ç³»ç»Ÿçš„é•œåƒ ID
             "InstanceType": "S5.2XLARGE16",  # é»˜è®¤å®žä¾‹è§„æ ¼ä¸ºæ ‡å‡†åž‹S6 2C4G
             "Placement": {
                 "Zone": "ap-tokyo-1"  # å¯ç”¨åŒº
             },
             "InstanceChargeType":  "PREPAID",  # æŒ‰å°æ—¶è®¡è´¹
             "SystemDisk": {
                 "DiskSize": 100,  # ç³»ç»Ÿç›˜å¤§å°
                 "DiskType": "CLOUD_SSD"  # ç³»ç»Ÿç›˜ç±»åž‹
             },
             "InternetAccessible": {
                 "InternetChargeType": "BANDWIDTH_PREPAID",  # æŒ‰æµé‡è®¡è´¹é»˜è®¤ä¸ç”¨ç»­è´¹
                 "InternetMaxBandwidthOut":  20,  # å‡ºå¸¦å®½ä¸Šé™
                 "PublicIpAssigned": True  # æ˜¯å¦åˆ†é…å…¬ç½‘ IP
             },
             "InstanceChargePrepaid": {
                 "Period": 1,  # é»˜è®¤è´­ä¹°æ—¶é—´ é»˜è®¤å•ä½æ˜¯æœˆ
                 "RenewFlag": "NOTIFY_AND_MANUAL_RENEW", # é»˜è®¤é€šçŸ¥è¿‡æœŸä¸è‡ªåŠ¨ç»­è´¹
             },
             "LoginSettings": {
                 "Password": "g8TJqBiUbSncYR2"  # é»˜è®¤ç™»å½•å¯†ç 
             },
             "InstanceName": "è¿ç»´æµ‹è¯•æ—¥æœ¬windosæœºå™¨-Johnny", #å¤‡æ³¨å®žä¾‹ä¿¡æ¯
             "EnhancedService": {  # å®žä¾‹å¢žå¼ºæœåŠ¡ç›¸å…³é…ç½®
                 "SecurityService": {  # å®‰å…¨æœåŠ¡
                     "Enabled": False,  # æ˜¯å¦å¼€å¯å®‰å…¨æœåŠ¡
                 },
         }
         }
         RequestResult = self.initTxCvmApi.CreateTxCloudCvmInstanceRequest(params)
         if RequestResult['status'] == True:
            print(f"""
                  åˆ›å»º{self.logo},äº‘æœåŠ¡å™¨æˆåŠŸ
                  {RequestResult}
            """)
         else:
             print(f"""
                  åˆ›å»º{self.logo},äº‘æœåŠ¡å™¨å¤±è´¥
                  {RequestResult}
             """)

     def StopCvmInstance(self,InstanceId=None):
         """
         åœæ­¢è…¾è®¯äº‘äº‘æœåŠ¡å™¨å®žä¾‹
         """
         RequestResult = self.initTxCvmApi.StopTxCloudCvmInstanceRequest(InstanceId=InstanceId)
         if RequestResult['status'] == True:
            print(f"""
                  åœæ­¢{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}æˆåŠŸ
                  {RequestResult}
            """)
         else:
             print(f"""
                  åœæ­¢{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}å¤±è´¥
                  {RequestResult}
             """)

     def DeleteCvmInstance(self,InstanceId=None):
         """
         åˆ é™¤è…¾è®¯äº‘äº‘æœåŠ¡å™¨å®žä¾‹
         """
         RequestResult = self.initTxCvmApi.DeleteTxCloudCvmInstanceRequest(InstanceId=InstanceId)
         if RequestResult['status'] == True:
            print(f"""
                  åˆ é™¤{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}æˆåŠŸ
                  {RequestResult}
            """)
         else:
             print(f"""
                  åˆ é™¤{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}å¤±è´¥
                  {RequestResult}
             """)

     def RenewCvmInstance(self,InstanceId=None,Period="1"):
         """
         ç»­è´¹è…¾è®¯äº‘äº‘æœåŠ¡å™¨å®žä¾‹
         é»˜è®¤ä¸ºä¸€ä¸ªæœˆ
         """
         RequestResult = self.initTxCvmApi.RenewTxCloudCvmInstanceRequest(InstanceId=InstanceId,Period=Period)
         if RequestResult['status'] == True:
            print(f"""
                  ç»­è´¹{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}æˆåŠŸ
                  {RequestResult}
            """)
         else:
             print(f"""
                  ç»­è´¹{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}å¤±è´¥
                  {RequestResult}
             """)

     def RebootCvmInstance(self,InstanceId=None):
         """
         é‡å¯è…¾è®¯äº‘äº‘æœåŠ¡å™¨å®žä¾‹
         """
         RequestResult = self.initTxCvmApi.RebootTxCloudCvmInstanceRequest(InstanceId=InstanceId)
         if RequestResult['status'] == True:
            print(f"""
                  é‡å¯{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}æˆåŠŸ
                  {RequestResult}
            """)
         else:
             print(f"""
                  é‡å¯{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}å¤±è´¥
                  {RequestResult}
             """)

     def StartCvmInstance(self,InstanceId=None):
         """
         å¯åŠ¨è…¾è®¯äº‘äº‘æœåŠ¡å™¨å®žä¾‹
         """
         RequestResult = self.initTxCvmApi.StartTxCloudCvmInstanceRequest(InstanceId=InstanceId)
         if RequestResult['status'] == True:
            print(f"""
                  å¯åŠ¨{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}æˆåŠŸ
                  {RequestResult}
            """)
         else:
             print(f"""
                  å¯åŠ¨{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹{InstanceId}å¤±è´¥
                  {RequestResult}
             """)

     def ResetCvmInstancesPassword(self,InstanceId=None):
         """
         ä¿®æ”¹è…¾è®¯äº‘äº‘æœåŠ¡å™¨å®žä¾‹å¯†ç 
         """
         UserName = input("è¯·è¾“å…¥éœ€è¦ä¿®æ”¹å¯†ç çš„ç”¨æˆ·å:")
         if UserName:
            UserName = UserName
         else:
            exit("è¾“å…¥ç”¨æˆ·åä¸ºç©º,è¯·é‡æ–°è¾“å…¥")
         Password = input(f"è¯·è¾“å…¥ç”¨æˆ·{UserName}éœ€è¦ä¿®æ”¹å¯†ç çš„:")
         if Password:
            Password = Password
         else:
             exit("è¾“å…¥å¯†ç ä¸ºç©º,è¯·é‡æ–°è¾“å…¥")
         RequestResult = self.initTxCvmApi.ResetTxCloudCvmInstancesPasswordRequest(InstanceId=InstanceId,Password=Password,
                        UserName=UserName)
         if RequestResult['status'] == True:
            print(f"""
                  ä¿®æ”¹{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹å¯†ç {InstanceId}æˆåŠŸ
                  {RequestResult}
            """)
         else:
             print(f"""
                  ä¿®æ”¹{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹å¯†ç {InstanceId}å¤±è´¥
                  {RequestResult}
             """)

     def GetCvmInstancesZons(self):
         """
         æŸ¥è¯¢è…¾è®¯äº‘å¯ç”¨åŒºåˆ—è¡¨
         éœ€è¦ä¼ å…¥region æŸ¥çœ‹åœ°åŒºå¯ç”¨åŒºåŸŸ
         """
         RequestResult = self.initTxCvmApi.GetCvmInstancesZonsRequest()
         if RequestResult['status'] == True:
            for ZonesInfo in RequestResult['message']:
                print(f"""
                       åŒºåŸŸåœ°åŒº  : {ZonesInfo.Zone}
                       åŒºåŸŸåç§°  : {ZonesInfo.ZoneName}
                       åŒºåŸŸID    : {ZonesInfo.ZoneId}
                       åŒºåŸŸçŠ¶æ€  : {ZonesInfo.ZoneState}
                """)
         else:
             print(f"""
                  æŸ¥è¯¢{self.logo},å¯ç”¨åŒºåŸŸå¤±è´¥
                  {RequestResult}
             """)

     def GetCvmInstancesState(self):
         """
         èŽ·å–å®žä¾‹çŠ¶æ€
         """
         RequestResult = self.initTxCvmApi.GetCvmInstancesStateRequest()
         if RequestResult['status'] == True:
            for InstancesInfo in RequestResult['message']:
                print(f"""
                     å®žä¾‹å    : {InstancesInfo.InstanceId}
                     å®žä¾‹çŠ¶æ€  : {InstancesInfo.InstanceState}
                """)
         else:
             print(f"""
                  æŸ¥è¯¢{self.logo},äº‘æœåŠ¡å™¨å®žä¾‹çŠ¶æ€å¤±è´¥
                  {RequestResult}
             """)

if __name__ == '__main__':
    """
    22222222222222222222222
    ins-mmhm66r2  æµ‹è¯•å®žä¾‹ID
    GetCvmInstancesState          èŽ·å–å®žä¾‹çŠ¶æ€
    ResetCvmInstancesPassword     ä¿®æ”¹å®žä¾‹å¯†ç 
    StopCvmInstance               å…³é—­å®žä¾‹
    StartCvmInstance              å¯åŠ¨å®žä¾‹
    RebootCvmInstance             é‡å¯å®žä¾‹
    GetInstanceList               èŽ·å–å®žä¾‹åˆ—è¡¨
    GetCvmImageList               èŽ·å–é•œåƒåˆ—è¡¨
    CreateInstance                åˆ›å»ºå®žä¾‹ 
    RenewCvmInstance              ç»­è´¹å®žä¾‹
    DeleteCvmInstance             åˆ é™¤å®žä¾‹
    """
    InstanceId = "ins-mmhm66r2"
    # region = "ap-tokyo"
    region = "ap-guangzhou"
    s = TxColudCvmOper(region=region)
    s.GetInstanceList()
    # s.RebootCvmInstance(InstanceId="ins-n1q1ah2g")
