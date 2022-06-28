from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SessionStarted
from datetime import date

import requests
import json
import urllib.request
from bs4 import BeautifulSoup
from pyvi import ViTokenizer, ViUtils
from underthesea import word_tokenize
import numpy as np


def tim_dn(s, d, t):
    for i in range(1, len(d) + 1):
        data = d[str(i)]
        dong_nghia = data["từ đồng nghĩa"]
        if s == data["đơn vị"]:
            return data[t]
        else:
            try:
                for j in range(len(dong_nghia)):
                    if dong_nghia[j] == s:
                        return data[t]
            except:
                continue
    return False


def lay_tt(s):
    dulieu = json.loads(s)
    text_kq = 'Thông tin hồ sơ:'
    tenhs = '\n+ Tên hồ sơ: ' + dulieu['tenhoso']
    text_kq = text_kq + tenhs
    ngay_tn = '\n+ Ngày tiếp nhận: ' + dulieu['ngaynhan']
    text_kq = text_kq + ngay_tn
    if dulieu['ngayhen'] is not None:
        ngayhen = '\n+ Ngày hẹn trả: ' + dulieu['ngayhen']
        text_kq = text_kq + ngayhen
    if dulieu['ngayxulyxong'] is not None:
        ngay_xlx = '\n+ Ngày xử lý xong: ' + dulieu['ngayxulyxong']
        text_kq = text_kq + ngay_xlx
    if dulieu['ngaytraketqua'] is not None:
        ngay_tkq = '\n+ Ngày trả kết quả: ' + dulieu['ngaytraketqua']
        text_kq = text_kq + ngay_tkq
    trang_thai = '\n+ Tình trạng xử lý hồ sơ: ' + dulieu['tinhtrang_hoso']
    text_kq = text_kq + trang_thai

    text_kq1 = 'Thông tin tổ chức/cá nhân: '
    ten = '\n+ Tên cơ quan: ' + dulieu['tccn_ten']
    text_kq1 = text_kq1 + ten
    diachi = '\n+ Địa chỉ: ' + dulieu['tccn_diachi']
    text_kq1 = text_kq1 + diachi
    if dulieu['socmnd'] != '0000000000':
        so_cmnd = '\n+ Số CMND: ' + dulieu['socmnd']
        text_kq1 = text_kq1 + so_cmnd
    if dulieu['nguoinhan'] is not None:
        nguoinhan = '\n+ Người nhận:' + dulieu['nguoinhan']
        text_kq1 = text_kq1 + nguoinhan

    return text_kq, text_kq1


class action_tra_cuu_hs(Action):
    def name(self):
        return 'action_tra_cuu_hs'

    def run(self, dispatcher, tracker, domain):

        ma_hs = next(tracker.get_latest_entity_values("ma_hs"), None)
        ma_hs = ma_hs.replace(" ", "")
        try:
            url = 'http://dichvucong.soctrang.gov.vn/api/hoso/tracuuhoso?tukhoa=' + ma_hs
            # Tien hanh lay thong tin tu URL
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            s = str(np.copy(str(soup)))
            return_msg, return_msg1 = lay_tt(s)

            dispatcher.utter_message(
                text='Hồ sơ bạn cần tìm có kết quả như sau: ')
            dispatcher.utter_message(text=return_msg)
            dispatcher.utter_message(text=return_msg1)
            dispatcher.utter_message(template="utter_restart")
            return [AllSlotsReset()]
        except:
            dispatcher.utter_message("Mã hồ sơ không tồn tại!")
            return [AllSlotsReset()]


class action_ss_started(Action):
    def name(self):
        return 'action_ss_started'

    def run(self, dispatcher, tracker, domain):
        return [SessionStarted()]


def lay_tttk(s):
    dulieu = json.loads(s)

    tl_thang = round(float(dulieu['tile_daxuly_thang']) * 100, 2)
    tl_nam = round(float(dulieu['tile_daxuly_nam']) * 100, 2)
    dunghan_thang = '\n+ Hồ sơ xử lý đúng hạn theo tháng: ' + \
        str(dulieu['hs_xldunghan_thang']) + '.'
    tile_thang = '\n+ Tỉ lệ đúng hạn theo tháng: ' + str(tl_thang) + '%' + '.'
    dunghan_nam = '\n+ Hồ sơ xử lý đúng hạn theo năm: ' + \
        str(dulieu['hs_xldunghan_nam']) + '.'
    tronghan_nam = '\n+ Hồ sơ xử lý trong hạn theo năm: ' + \
        str(dulieu['hs_tronghan_nam']) + '.'
    trehan_thang = '\n+ Hồ sơ xử lý trễ hạn theo tháng: ' + \
        str(dulieu['hs_xl_trehan_thang']) + '.'
    tile_nam = '\n+ Tỉ lệ đúng hạn theo năm: ' + str(tl_nam) + '%' + '.'
    tronghan_thang = '\n+ Hồ sơ xử lý trong hạn theo tháng: ' + \
        str(dulieu['hs_tronghan_thang']) + '.'
    moi_thang = '\n+ Hồ sơ mới tiếp nhận theo tháng: ' + \
        str(dulieu['hs_moitiepnhan_thang']) + '.'
    moi_nam = '\n+ Hồ sơ mới tiếp nhận theo năm: ' + \
        str(dulieu['hs_moitiepnhan_nam']) + '.'
    trehan_nam = '\n+ Hồ sơ xử lý trễ hạn năm: ' + \
        str(dulieu['hs_xl_trehan_nam']) + '.'

    text_kq = moi_thang + dunghan_thang + tronghan_thang + trehan_thang + tile_thang
    return text_kq


class action_thong_ke_full(Action):
    def name(self):
        return 'action_thong_ke_full'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        thang = tracker.get_slot("thang_tk")
        thang = thang.replace(" ", "")
        nam = tracker.get_slot("nam_tk")
        nam = nam.replace(" ", "")
        donvi_cb = tracker.get_slot("don_vi")
        nam_ht = date.today().year
        thang_ht = date.today().month

        if int(nam) > nam_ht or (nam_ht == int(nam) and int(thang) > thang_ht):
            # dispatcher.utter_message(text="Xin lỗi hiện tại chỉ là tháng {} năm {}!".format(thang_ht, nam_ht))
            # dispatcher.utter_message(template="utter_restart")
            return [AllSlotsReset()]

        with open('data_full.json', encoding='utf8') as file_write:
            d = json.load(file_write)
        try:
            domain = tim_dn(donvi_cb, d, "domain")
            # print(domain, ' ', thang, ' ', nam)
            try:
                domain = domain.replace("motcua.", "motcua")
            except:
                domain = domain
            url = 'https://dichvucong.soctrang.gov.vn/api/lienthongiso/tkttxlhs?domain=' + domain \
                  + '&thang=' + thang + '&nam=' + nam

            print(url)
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            s = str(np.copy(str(soup)))
            return_msg = lay_tttk(s)

            dispatcher.utter_message(text="Kết quả thống kê của " + donvi_cb.title() + " vào tháng " + thang + " năm "
                                          + nam + " có kết quả như sau: " + return_msg)
        except:
            dispatcher.utter_message(template="utter_loi")
        dispatcher.utter_message(template="utter_restart")
        return [AllSlotsReset()]


class action_tra_cuu_diachi(Action):
    def name(self):
        return 'action_tra_cuu_diachi'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        donvi_cb = tracker.get_slot("don_vi")
        donvi_cb = donvi_cb.lower()
        hoi_ttin = tracker.get_slot("hoi_tt")
        hoi_ttin = hoi_ttin.lower()
        with open('data_full.json', encoding='utf-8') as file_write:
            d = json.load(file_write)
        donvi = tim_dn(donvi_cb, d, "đơn vị")
        diaChi = tim_dn(donvi_cb, d, "địa chỉ")
        soDT = tim_dn(donvi_cb, d, "số điện thoại")
        soFax = tim_dn(donvi_cb, d, "số fax")
        dcEmail = tim_dn(donvi_cb, d, "email")
        if hoi_ttin == 'địa chỉ':
            dispatcher.utter_message(text="Địa chỉ của đơn vị " + donvi.title() +
                                          ": " + diaChi)
        if hoi_ttin == 'số điện thoại':
            dispatcher.utter_message(text="Số điện thoại của đơn vị " + donvi.title() +
                                          ": " + soDT)
        if hoi_ttin == 'fax':
            dispatcher.utter_message(text="Số Fax của đơn vị " + donvi.title() +
                                          ": " + soFax)
        if hoi_ttin == 'email':
            dispatcher.utter_message(text="Địa chỉ email của đơn vị " + donvi.title() +
                                          ": " + dcEmail)
        if hoi_ttin == 'full_tt':
            # text_kq = "Thông tin của đơn vị " + donvi.title() + " như sau: " + "\n+ Địa chỉ: " + diaChi + \
            #           "\n+ Số điện thoại: " + soDT + "\n+ Số Fax: " + soFax + "\n+ Email: " + dcEmail
            data = [{'title': 'Địa chỉ', 'description': diaChi},
                    {'title': 'Số điện thoại', 'description': soDT},
                    {'title': 'Số Fax', 'description': soFax},
                    {'title': 'Email', 'description': dcEmail}]
            message = {"payload": "list_show", "data": data}
            dispatcher.utter_message(
                text="Thông tin của đơn vị " + donvi.title() + " như sau:", json_message=message)

        dispatcher.utter_message(template="utter_restart")
        return [AllSlotsReset()]


class action_greet(Action):
    def name(self):
        return 'action_greet'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Chào bạn, Tôi là hệ thống Dịch vụ công Sóc Trăng.")
        dispatcher.utter_message(template="utter_chuc_nang")
        return []


class action_get_started(Action):
    def name(self):
        return 'action_get_started'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Chào bạn, Tôi là hệ thống Dịch vụ công Sóc Trăng.")
        dispatcher.utter_message(template="utter_get_started")
        return []


class thongke_form(FormAction):
    def name(self) -> Text:
        return "thongke_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["don_vi", "thang_tk", "nam_tk"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "don_vi": self.from_entity(entity="don_vi", intent=["thong_ke", "chi_co_dv"]),
            "thang_tk": self.from_entity(entity="thang_tk", intent=["inform", "thong_ke"]),
            "nam_tk": self.from_entity(entity="nam_tk", intent=["inform", "thong_ke"]),
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_thang_tk(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if np.shape(value) != ():
            value = value[0]
        if self.is_int(value) and int(value) > 0:
            if int(value) <= 12:
                return {"thang_tk": value}
            else:
                dispatcher.utter_message(template="utter_saithang")
                return {"thang_tk": None}

    def validate_nam_tk(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if np.shape(value) != ():
            value = value[0]
        t_tk = tracker.get_slot('thang_tk')

        nam_ht = date.today().year
        thang_ht = date.today().month
        if int(value) > nam_ht:
            dispatcher.utter_message(
                "Xin lỗi! Hiện tại chỉ là năm " + str(nam_ht) + "!")
            return {"nam_tk": None}
        if t_tk is None:
            return {"thang_tk": None}
        if int(value) == nam_ht and int(t_tk) > thang_ht:
            dispatcher.utter_message("Xin lỗi, hiện tại chỉ là tháng " + str(thang_ht) + " năm " +
                                     str(nam_ht) + "!")
            dispatcher.utter_message(
                "Vui lòng nhập lại thời gian bạn cần thống kê!")
            return {"thang_tk": None,
                    "nam_tk": value}
        return {"nam_tk": value}


    def validate_don_vi(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        with open('data_full.json', encoding='utf8') as file_write:
            d = json.load(file_write)
        if np.shape(value) != ():
            value = value[0]

        value = value.lower()
        if tim_dn(value, d, "đơn vị"):
            donvi = tim_dn(value, d, "đơn vị")
            return {"don_vi": donvi}
        else:
            dispatcher.utter_message(template="utter_saidv")
            return {"don_vi": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_message(template="utter_thong_ke")
        return []


class action_setslot(Action):
    def name(self):

        return 'action_setslot'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'hoi_dc':
            return [SlotSet("hoi_tt", "địa chỉ")]
        if intent == 'hoi_sdt':
            return [SlotSet("hoi_tt", "số điện thoại")]
        if intent == 'hoi_fax':
            return [SlotSet("hoi_tt", "fax")]
        if intent == 'hoi_email':
            return [SlotSet("hoi_tt", "email")]
        if intent == 'full_tt':
            return [SlotSet("hoi_tt", "full_tt")]


class action_rsslot(Action):
    def name(self):
        return 'action_rsslot'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        return [AllSlotsReset()]


class diachi_form(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "diachi_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["don_vi", "hoi_tt"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "don_vi": self.from_entity(entity="don_vi", intent=["tra_cuu_diachi",
                                                                "chi_co_dv", "hoi_dc", "hoi_sdt",
                                                                "hoi_fax", "hoi_email", "full_tt"]),
            "hoi_tt": [
                self.from_intent(value="địa chỉ", intent=["hoi_dc"]),
                self.from_intent(value="số điện thoại", intent=["hoi_sdt"]),
                self.from_intent(value="fax", intent=["hoi_fax"]),
                self.from_intent(value="email", intent=["hoi_email"]),
                self.from_intent(value="full_tt", intent=["full_tt"]),
            ]
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_don_vi(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        with open('data_full.json', encoding='utf8') as file_write:
            d = json.load(file_write)
        if np.shape(value) != ():
            value = value[0]

        value = value.lower()
        # print(value)
        if tim_dn(value, d, "đơn vị"):
            donvi = tim_dn(value, d, "đơn vị")
            return {"don_vi": donvi}
        else:
            dispatcher.utter_message(template="utter_saidv")
            return {"don_vi": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        return []


class mahs_form(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "mahs_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["ma_hs"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "ma_hs": self.from_entity(entity="ma_hs", intent=["tra_cuu_hs", "inform"])
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        return []


class thutuc_form(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "thutuc_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["don_vi", "tu_khoa"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "don_vi": self.from_entity(entity="don_vi", intent=["chi_co_dv"]),
            "tu_khoa": self.from_text(intent=["ten_thu_tuc"])
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_don_vi(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        with open('data_full.json', encoding='utf8') as file_write:
            d = json.load(file_write)
        if np.shape(value) != ():
            value = value[0]

        value = value.lower()
        if tim_dn(value, d, "đơn vị"):
            donvi = tim_dn(value, d, "đơn vị")
            return {"don_vi": donvi}
        else:
            dispatcher.utter_message(template="utter_saidv")
            return {"don_vi": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        return []


class action_show_thutuc(Action):
    def name(self):
        return 'action_show_thutuc'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        with open('data_full.json', encoding='utf8') as file_write:
            d = json.load(file_write)
        key = tracker.get_slot("key_tt")
        # url = 'http://127.0.0.1:105/tracuu/timtt/tim&idtt=' + key
        # page = urllib.request.urlopen(url)
        # soup = BeautifulSoup(page, 'html.parser')
        # stri = str(np.copy(str(soup)))
        # dulieu = json.loads(stri)
        url = 'http://localhost:8000/thutuc'
        data_up = {'id_tt': str(key)}
        du_lieu = requests.post(url, data=json.dumps(data_up))
        du_lieu = du_lieu.json()
        for matt in du_lieu.keys():
            thongtin = str(du_lieu[matt])
            thongtin = json.loads(thongtin.replace("\'", "\""))
            dv_id = thongtin['dv_id']
            for i in range(1, len(d) + 1):
                data = d[str(i)]
                if str(dv_id) == str(data['id']):
                    dv_url = data['domain']
                    break
            link = 'http://' + dv_url + '/home?tt_ma=' + matt
            print(link)
            # string_thu_tuc = 'Tên thủ tục: \n' + thongtin['Thủ tục tên'].upper() + \
            #                  '\n+ Thời gian giải quyết: \n' + thongtin['Thời gian giải quyết'] + \
            #                  '\n+ Cách thức thực hiện: \n' + thongtin['Cách thức thực hiện'] + \
            #                  '\n+ Xem chi tiết: \n ' + link
            data = [{'title': 'Thời gian giải quyết', 'description': thongtin['Thời gian giải quyết']},
                    {'title': 'Cách thức thực hiện',
                        'description': thongtin['Cách thức thực hiện']},
                    {'title': 'Xem chi tiết', 'description': '<a href = ' + link + ' target="_blank"> Xem </a>'}]
            message = {"payload": "collapsible", "data": data}
            dispatcher.utter_message(
                text='Thông tin thủ tục \n' + thongtin['Thủ tục tên'].upper() + ' như sau:', json_message=message)
        dispatcher.utter_message(template="utter_restart")
        return [AllSlotsReset()]


class action_thu_tuc(Action):
    def name(self):

        return 'action_thu_tuc'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        try:
            donvi_cb = tracker.get_slot("don_vi")
            tukhoa = tracker.get_slot("tu_khoa")
            tukhoa = tukhoa[8:]
            with open('data_full.json', encoding='utf8') as file_write:
                d = json.load(file_write)

            iddv = tim_dn(donvi_cb, d, "id")
            if not iddv:
                iddv = 0
            idlv = 0
            s1 = ViTokenizer.spacy_tokenize(tukhoa)

            dic = {}
            for i in range(len(s1[0])):
                tk = s1[0][i]
                # tk = s1[i]
                tk = tk.replace('_', ' ')
                # tk = str(ViUtils.remove_accents(tk))
                # url = 'http://127.0.0.1:105/tracuu/thutuc/laythutuc&iddv=' + str(iddv) + '&idlv=' + str(
                #     idlv) + '&tukhoa=' + tk[2:-1]
                # page = urllib.request.urlopen(url)
                # soup = BeautifulSoup(page, 'html.parser')
                # stri = str(np.copy(str(soup)))
                # dulieu = json.loads(stri)
                url = 'http://localhost:8000/lay_thu_tuc'
                data_up = {'id_dv': str(iddv),
                           'id_lv': str(idlv),
                           'tu_khoa': tk}
                du_lieu = requests.post(url, data=json.dumps(data_up))
                du_lieu = du_lieu.json()
                for key in du_lieu.keys():
                    if key in dic.keys():
                        dic[key] += 1
                    else:
                        dic.update({key: 0})
            print(tukhoa)
            # print(dic)
            if len(dic.values()) < 1:
                dispatcher.utter_message(
                    text='Xin lỗi! Không tìm thấy thủ tục bạn cần tìm')
                return [AllSlotsReset()]

            ds_matt = []
            buttons = []
            for key, value in dic.items():
                if value == max(dic.values()):
                    # url = 'http://127.0.0.1:105/tracuu/timtt/tim&idtt=' + key
                    # print(url)
                    # page = urllib.request.urlopen(url)
                    # soup = BeautifulSoup(page, 'html.parser')
                    # stri = str(np.copy(str(soup)))
                    # dulieu = json.loads(stri)
                    url = 'http://localhost:8000/thutuc'
                    data_up = {'id_tt': str(key)}
                    du_lieu = requests.post(url, data=json.dumps(data_up))
                    du_lieu = du_lieu.json()
                    for matt in du_lieu.keys():
                        try:
                            ds_matt.index(matt)
                        except:
                            ds_matt.append(matt)
                            thongtin = str(du_lieu[matt])
                            thongtin = json.loads(thongtin.replace("\'", "\""))

                            sss = '/show_thutuc{"key_tt":"' + key + '"}'
                            buttons.append(
                                {'title': thongtin['Thủ tục tên'], 'payload': sss})
            dispatcher.utter_button_message(
                'Chọn thủ tục mà bạn cần: ', buttons=buttons)
        except:
            dispatcher.utter_message(template="utter_loi")
        return [AllSlotsReset()]

# tracuu_hs_tccn
# show ho so


class action_tra_cuu_hs_tccn(Action):
    def name(self):
        return 'action_tra_cuu_hs_tccn'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        ngay = tracker.get_slot("ngay_tk")
        ngay = ngay.replace(" ", "")
        thang = tracker.get_slot("thang_tk")
        thang = thang.replace(" ", "")
        nam = tracker.get_slot("nam_tk")
        nam = nam.replace(" ", "")
        thoigian = nam + "-" + thang + "-" + ngay
        tccn = tracker.get_slot("tc_cn")
        nam_ht = date.today().year
        thang_ht = date.today().month

        if int(nam) > nam_ht or (nam_ht == int(nam) and int(thang) > thang_ht):
            return [AllSlotsReset()]

        # try:
        if not tccn:
            tccn = 0
        s1 = ViTokenizer.spacy_tokenize(thoigian)

        dic = {}

        for i in range(len(s1[0])):
            url = 'http://localhost:8000/hoso'
            data_up = {'ten_DN': str(tccn),
                       'thoi_gian': thoigian}
            du_lieu = requests.post(url, data=json.dumps(data_up))
            du_lieu = du_lieu.json()
            for hs in du_lieu.keys():
                if hs in dic.keys():
                    dic[hs] += 1
                else:
                    dic.update({hs: 0})
        print(thoigian)
        if len(dic.values()) < 1:
            dispatcher.utter_message(
                text='Xin lỗi! Không tìm thấy hồ sơ bạn cần tìm')
            return [AllSlotsReset()]
        ds_hs = []
        buttons = []
        url = 'http://localhost:8000/hoso'
        data_up = {'ten_DN': str(tccn),
                   'thoi_gian': thoigian}
        print(data_up)
        du_lieu = requests.post(url, data=json.dumps(data_up))
        du_lieu = du_lieu.json()
        (du_lieu)
        for hs in du_lieu.keys():
            try:
                ds_hs.index(hs)
            except:
                ds_hs.append(hs)
                thongtin = str(du_lieu[hs])
                thongtin = json.loads(thongtin.replace("\'", "\""))
        #                 sss = '/show_hoso'
        #                 buttons.append(
        #                     {'title': thongtin['noidung'], 'payload': sss})
        # dispatcher.utter_button_message(
        #     'Chọn hồ sơ mà bạn cần: ', buttons=buttons)
                # data = [{'title': 'Ngày tiếp nhận', 'description': thongtin['ngaytiepnhan']},
                #         {'title': 'Ngày hẹn trả',
                #         'description': thongtin['ngayhentra']},
                #         {'title': 'Ngày trả kết quả',
                #         'description': thongtin['ngaytrakq']},
                #         {'title': 'Ngày xử lý xong',
                #         'description': thongtin['ngayxulyxong']},
                #         {'title': 'Tình trạng hồ sơ',
                #         'description': thongtin['tinhtranghs']},
                #         {'title': 'Người tiếp nhận',
                #         'description': thongtin['nguoitiepnhan']},
                #         {'title': 'Tên tổ chức cá nhân',
                #         'description': thongtin['tccn_ten']},
                #         {'title': 'Địa chỉ',
                #         'description': thongtin['diachi_tccn']},
                #         {'title': 'Ngày tạo hồ sơ',
                #         'description': thongtin['hs_ngaytao']},
                #         {'title': 'Mã hồ sơ',
                #         'description': thongtin['hs_ma']}
                #         ]
                # message = {"payload": "collapsible", "data": data}
                # dispatcher.utter_message(
                hoso_msg = '\n+ Ngày tiếp nhận: \n' + thongtin['ngaytiepnhan'] + \
                    '\n+ Ngày hẹn trả: \n' + thongtin['ngayhentra'] + \
                    '\n+ Ngày trả kết quả: \n' + thongtin['ngaytrakq'] + \
                    '\n+ Ngày xử lý xong: \n' + thongtin['ngayxulyxong'] + \
                    '\n+ Tình trạng hồ sơ: \n' + thongtin['tinhtranghs'] + \
                    '\n+ Người tiếp nhận: \n' + thongtin['nguoitiepnhan'] + \
                    '\n+ Tên tổ chức cá nhân: \n' + thongtin['tccn_ten'] + \
                    '\n+ Địa chỉ: \n' + thongtin['diachi_tccn'] + \
                    '\n+ Ngày tạo hồ sơ: \n' + thongtin['hs_ngaytao'] + \
                    '\n+ Mã hồ sơ: \n' + thongtin['hs_ma']
                dispatcher.utter_message(
                    text='Thông tin hồ sơ \n' + thongtin['noidung'].upper() + ' như sau: ' + hoso_msg)
        dispatcher.utter_message(template="utter_restart")
        return [AllSlotsReset()]


class action_show_hoso(Action):
    def name(self):
        return 'action_show_hoso'

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        ngay = tracker.get_slot("ngay_tk")
        ngay = ngay.replace(" ", "")
        thang = tracker.get_slot("thang_tk")
        thang = thang.replace(" ", "")
        nam = tracker.get_slot("nam_tk")
        nam = nam.replace(" ", "")
        thoigian = nam + "-" + thang + "-" + ngay
        tccn = tracker.get_slot("tc_cn")
        nam_ht = date.today().year
        thang_ht = date.today().month
        url = 'http://localhost:8000/hoso'
        data_up = {'ten_DN': str(tccn),
                   'thoi_gian': thoigian}
        du_lieu = requests.post(url, data=json.dumps(data_up))
        du_lieu = du_lieu.json()
        for hs in du_lieu.keys():
            thongtin = str(du_lieu[hs])
            thongtin = json.loads(thongtin.replace("\'", "\""))
            hoso_msg = '\n+ Ngày tiếp nhận: \n' + thongtin['ngaytiepnhan'] + \
                '\n+ Ngày hẹn trả: \n' + thongtin['ngayhentra'] + \
                '\n+ Ngày trả kết quả: \n' + thongtin['ngaytrakq'] + \
                '\n+ Ngày xử lý xong: \n' + thongtin['ngayxulyxong'] + \
                '\n+ Tình trạng hồ sơ: \n' + thongtin['tinhtranghs'] + \
                '\n+ Người tiếp nhận: \n' + thongtin['nguoitiepnhan'] + \
                '\n+ Tên tổ chức cá nhân: \n' + thongtin['tccn_ten'] + \
                '\n+ Địa chỉ: \n' + thongtin['diachi_tccn'] + \
                '\n+ Ngày tạo hồ sơ: \n' + thongtin['hs_ngaytao'] + \
                '\n+ Mã hồ sơ: \n' + thongtin['hs_ma']
            dispatcher.utter_message(
                text='Thông tin hồ sơ \n' + thongtin['noidung'].upper() + ' như sau: ' + hoso_msg)
        dispatcher.utter_message(template="utter_restart")
        return [AllSlotsReset()]


class tccn_form(FormAction):
    def name(self) -> Text:
        return "tccn_form"

    @ staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["tc_cn", "ngay_tk", "thang_tk", "nam_tk"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "tc_cn": self.from_entity(entity="tc_cn", intent=["tra_cuu_hs_tccn"]),
            "ngay_tk": self.from_entity(entity="ngay_tk", intent=["inform", "tra_cuu_hs_tccn"]),
            "thang_tk": self.from_entity(entity="thang_tk", intent=["inform", "tra_cuu_hs_tccn"]),
            "nam_tk": self.from_entity(entity="nam_tk", intent=["inform", "tra_cuu_hs_tccn"]),

        }

    @ staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_ngay_tk(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if np.shape(value) != ():
            value = value[0]
        if self.is_int(value) and int(value) > 0:
            if int(value) <= 31:
                return {"ngay_tk": value}
            else:
                dispatcher.utter_message(template="utter_saingay")
                return {"ngay_tk": None}

    def validate_thang_tk(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if np.shape(value) != ():
            value = value[0]
        if self.is_int(value) and int(value) > 0:
            if int(value) <= 12:
                return {"thang_tk": value}
            else:
                dispatcher.utter_message(template="utter_saithang")
                return {"thang_tk": None}

    def validate_nam_tk(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if np.shape(value) != ():
            value = value[0]
        t_tk = tracker.get_slot('thang_tk')

        nam_ht = date.today().year
        thang_ht = date.today().month
        if self.is_int(value) and 0 < int(value) <= nam_ht:
            if t_tk is None:
                return {"thang_tk": None}
            if int(t_tk) > thang_ht:
                dispatcher.utter_message("Xin lỗi, hiện tại chỉ là tháng " + str(thang_ht) + " năm " +
                                         str(nam_ht) + "!")
                dispatcher.utter_message(
                    "Vui lòng nhập lại thời gian bạn cần tra cứu!")
                return {"thang_tk": None}
            return {"nam_tk": value}
        elif int(value) > nam_ht:
            dispatcher.utter_message(
                "Xin lỗi! Hiện tại chỉ là năm " + str(nam_ht) + "!")
            return {"nam_tk": None}
        else:
            dispatcher.utter_message(template="utter_sainam")
            # validation failed, set slot to None
            return {"nam_tk": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_message(template="utter_tc_cn")
        return []
