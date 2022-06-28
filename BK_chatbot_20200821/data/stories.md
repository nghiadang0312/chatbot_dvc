##thong_ke
* thong_ke
  - thongke_form
  - form{"name": "thongke_form"}
  - form{"name": null}
  - action_thong_ke_full
  - action_rsslot
  - slot{"requested_slot": null}

##dia chi
* tra_cuu_diachi
  - diachi_form
  - form{"name": "diachi_form"}
  - form{"name": null}
  - action_tra_cuu_diachi
  - action_rsslot
  - slot{"requested_slot": null}

##dc1
* hoi_dc
  - action_setslot
  - diachi_form
  - form{"name": "diachi_form"}
  - form{"name": null}
  - action_tra_cuu_diachi
  - action_rsslot
  - slot{"requested_slot": null}

##dc2
* hoi_sdt
  - action_setslot
  - diachi_form
  - form{"name": "diachi_form"}
  - form{"name": null}
  - action_tra_cuu_diachi
  - action_rsslot
  - slot{"requested_slot": null}

##dc3
* hoi_fax
  - action_setslot
  - diachi_form
  - form{"name": "diachi_form"}
  - form{"name": null}
  - action_tra_cuu_diachi
  - action_rsslot
  - slot{"requested_slot": null}

##dc4
* hoi_email
  - action_setslot
  - diachi_form
  - form{"name": "diachi_form"}
  - form{"name": null}
  - action_tra_cuu_diachi
  - action_rsslot
  - slot{"requested_slot": null}

##dc5
* full_tt
  - action_setslot
  - diachi_form
  - form{"name": "diachi_form"}
  - form{"name": null}
  - action_tra_cuu_diachi
  - action_rsslot
  - slot{"requested_slot": null}

##chi co don vi
* chi_co_dv
  - utter_chi_co_dv

##chao
* greet
  - action_greet

##tam biet
* bye
  - utter_bye
  - action_rsslot
  - action_ss_started

## chuc nang
* chuc_nang
  - utter_chuc_nang

## bat dau
* get_started
  - action_get_started

##k ý nghĩa
* k_y_nghia
  - utter_fallback

## st1
* thong_ke{"don_vi":"sở công thương","thang_tk":"7","nam_tk":"2020"}
    - slot{"don_vi":"sở công thương"}
    - slot{"nam_tk":"2020"}
    - slot{"thang_tk":"7"}
    - action_thong_ke_full

## thoat form ma hs
* greet
    - action_greet
* tra_cuu_hs_tccn
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}
* greet
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_greet
* tra_cuu_diachi
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"requested_slot":"don_vi"}
* chi_co_dv{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"ban dân tộc"}
    - diachi_form
    - slot{"don_vi":"ban dân tộc"}
    - slot{"requested_slot":"hoi_tt"}
    - diachi_form
    - slot{"hoi_tt":"email"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_tra_cuu_diachi
* bye
    - utter_bye
    - action_ss_started

## thoat form tk1

* greet
    - action_greet
* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* greet
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_greet

## thoat form tt 1

* greet
    - action_greet
* tra_cuu_diachi
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"requested_slot":"don_vi"}
* greet
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_greet

## thoat form mahs2

* greet
    - action_greet
* tra_cuu_hs_tccn
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}
* thong_ke
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* chi_co_dv{"don_vi":"sở y tế"}
    - slot{"don_vi":"sở y tế"}
    - thongke_form
    - slot{"don_vi":"sở y tế"}
    - slot{"requested_slot":"thang_tk"}
* inform{"thang_tk":"7","nam_tk":"2020"}
    - slot{"nam_tk":"2020"}
    - slot{"thang_tk":"7"}
    - thongke_form
    - slot{"nam_tk":"2020"}
    - slot{"thang_tk":"7"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_thong_ke_full
* bye
    - utter_bye
    - action_ss_started

## st3
* tra_cuu_diachi
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"requested_slot":"don_vi"}
* thong_ke{"don_vi":"sở công thương"}
    - slot{"don_vi":"sở công thương"}
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"don_vi":"sở công thương"}
    - slot{"don_vi":"sở công thương"}
    - slot{"requested_slot":"thang_tk"}
* inform{"thang_tk":"12","nam_tk":"2019"}
    - slot{"nam_tk":"2019"}
    - slot{"thang_tk":"12"}
    - thongke_form
    - slot{"nam_tk":"2019"}
    - slot{"thang_tk":"12"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_thong_ke_full
* bye
    - utter_bye
    - action_ss_started

## st4
* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* tra_cuu_hs_tccn
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}

## st5


* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* tra_cuu_diachi
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"requested_slot":"don_vi"}

## st6


* tra_cuu_diachi
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"requested_slot":"don_vi"}
* chuc_nang
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_chuc_nang

## st7

* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* chuc_nang
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_chuc_nang

## st8


* tra_cuu_hs_tccn
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}
* chuc_nang
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_chuc_nang

## st9


* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* hoi_dc
    - action_setslot
    - slot{"hoi_tt":"địa chỉ"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_greet
* tra_cuu_diachi
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"hoi_tt":"địa chỉ"}
    - slot{"requested_slot":"don_vi"}
    - slot{"don_vi":"sở công thương"}
    - diachi_form
    - slot{"don_vi":"sở công thương"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_tra_cuu_diachi
* bye
    - utter_bye
    - action_ss_started

## st11

* tra_cuu_hs_tccn
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}
* k_y_nghia
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}

<!-- ## st12


* tra_cuu_hs
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
* inform{"thang_tk":"213123"}
    - slot{"thang_tk":"213123"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"} -->

<!-- ## st13


* tra_cuu_hs
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
* chi_co_dv{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"ban dân tộc"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
* chi_co_dv{"don_vi":"sở công thương"}
    - slot{"don_vi":"sở công thương"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"sở công thương"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
* inform{"thang_tk":"2323"}
    - slot{"thang_tk":"2323"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
    - slot{"ma_hs":"000.00.04.H51-200221-0001"}
    - mahs_form
    - slot{"ma_hs":"000.00.04.H51-200221-0001"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_tra_cuu_hs
* bye
    - utter_bye
    - action_ss_started -->

<!-- ## st14

* tra_cuu_hs
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
* chi_co_dv{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"ban dân tộc"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
* greet
    - slot{"don_vi":"ban dân tộc"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_greet -->

## st15

* tra_cuu_hs_tccn
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}
* chuc_nang
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_chuc_nang

## st16

* tra_cuu_hs_tccn
    - tccn_form
    - form{"name":"tccn_form"}
    - slot{"requested_slot":"tc_cn"}
* bye
    - utter_bye
    - action_rsslot

## st17

* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* chuc_nang
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_chuc_nang
* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* bye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_bye
    - action_rsslot

## st18

<!-- * greet
    - action_greet
* tra_cuu_hs
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"}
* inform{"thang_tk":"321"}
    - slot{"thang_tk":"321"}
    - slot{"thang_tk":"321"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - mahs_form
    - form{"name":"mahs_form"}
    - slot{"requested_slot":"ma_hs"} -->
* greet
    - slot{"thang_tk":"321"}
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_rsslot
    - action_greet
* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"requested_slot":"don_vi"}
* chi_co_dv{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"ban dân tộc"}
    - thongke_form
    - slot{"don_vi":"ban dân tộc"}
    - slot{"requested_slot":"thang_tk"}
    - slot{"nam_tk":"2019"}
    - slot{"thang_tk":"8"}
    - thongke_form
    - slot{"nam_tk":"2019"}
    - slot{"thang_tk":"8"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_thong_ke_full
* bye
    - utter_bye
    - action_rsslot

## New Story

* chi_co_dv{"don_vi":"sở gddt"}
    - slot{"don_vi":"sở gddt"}
    - utter_chi_co_dv
* tra_cuu_diachi
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"don_vi":"sở giáo dục và đào tạo"}
    - slot{"requested_slot":"hoi_tt"}
* full_tt
    - diachi_form
    - slot{"hoi_tt":"full_tt"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_tra_cuu_diachi
    - action_rsslot

## New Story

* chi_co_dv{"don_vi":"sở công thương"}
    - slot{"don_vi":"sở công thương"}
    - utter_chi_co_dv
* thong_ke
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"don_vi":"sở công thương"}
    - slot{"requested_slot":"thang_tk"}
* inform{"thang_tk":"10","nam_tk":"2019"}
    - slot{"nam_tk":"2019"}
    - slot{"thang_tk":"10"}
    - thongke_form
    - slot{"nam_tk":"2019"}
    - slot{"thang_tk":"10"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_thong_ke_full

## New Story

* tra_cuu_diachi{"don_vi":"ban dân tộc sóc trăng"}
    - slot{"don_vi":"ban dân tộc sóc trăng"}
    - diachi_form
    - form{"name":"diachi_form"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"requested_slot":"hoi_tt"}
* full_tt
    - diachi_form
    - slot{"hoi_tt":"full_tt"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_tra_cuu_diachi
    - action_rsslot

## New Story

* thong_ke{"don_vi":"ban dân tộc","thang_tk":"7"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"thang_tk":"7"}
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"thang_tk":"7"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"thang_tk":"7"}
    - slot{"requested_slot":"nam_tk"}
    - slot{"nam_tk":"2020"}
    - thongke_form
    - slot{"nam_tk":"2020"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_thong_ke_full
* bye
    - utter_bye
    - action_ss_started

## New Story

* thong_ke{"don_vi":"ban dân tộc","nam_tk":"2020"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"nam_tk":"2020"}
    - thongke_form
    - form{"name":"thongke_form"}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"nam_tk":"2020"}
    - slot{"thang_tk":null}
    - slot{"don_vi":"ban dân tộc"}
    - slot{"nam_tk":"2020"}
    - slot{"thang_tk":null}
    - slot{"requested_slot":"thang_tk"}
* inform{"thang_tk":"7"}
    - slot{"thang_tk":"7"}
    - thongke_form
    - slot{"thang_tk":"7"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_thong_ke_full
* bye
    - utter_bye
    - action_ss_started

## cảm ơn
* cam_on
	- utter_cam_on
    - action_rsslot

## xin lỗi
* xin_loi
	- utter_xin_loi
    - action_rsslot

## thu tuc
* thu_tuc
    - thutuc_form
    - form{"name": "thutuc_form"}
    - form{"name": null}
    - action_thu_tuc
    - action_rsslot
    - slot{"requested_slot": null}

## thu tuc theo ma
* show_thutuc
	- thutuc_form
    - form{"name": "thutuc_form"}
    - form{"name": null}
    - action_show_thutuc
    - action_rsslot
    - slot{"requested_slot": null}

## New Story

* thu_tuc
    - thutuc_form
    - form{"name":"thutuc_form"}
    - slot{"requested_slot":"don_vi"}
    - slot{"don_vi":"huyện mỹ xuyên"}
* chi_co_dv{"don_vi":"huyện mỹ xuyên"}
    - thutuc_form
    - slot{"don_vi":"huyện mỹ xuyên"}
* ten_thu_tuc
    - thutuc_form
    - form{"name":null}
    - slot{"tu_khoa":"thủ tục đăng ký hợp tác xã sáp nhập"}
    - action_thu_tuc
    - action_rsslot
    - slot{"key_tt":"129020"}
* show_thutuc{"key_tt":"129020"}
    - action_show_thutuc

## Story from conversation with 7486d68f8d0846849005e93db58fdcea on September 8th 2020

* get_started
    - action_get_started
* thu_tuc
    - thutuc_form
    - form{"name":"thutuc_form"}
    - slot{"requested_slot":"don_vi"}
    - slot{"don_vi":"huyện mỹ xuyên"}
* chi_co_dv{"don_vi":"huyện mỹ xuyên"}
    - slot{"don_vi":"huyện mỹ xuyên"}
    - thutuc_form
    - slot{"don_vi":"huyện mỹ xuyên"}
* ten_thu_tuc
    - thutuc_form
    - form{"name":null}
    - slot{"tu_khoa":"thủ tục giải quyết tranh chấp đất đai cấp huyện"}
    - action_thu_tuc
    - action_rsslot
    - slot{"key_tt":"128977"}
* show_thutuc{"key_tt":"128977"}
    - slot{"key_tt":"128977"}
    - action_show_thutuc
* bye
    - utter_bye
    - action_rsslot

## Story from conversation with 0115ca6e7f104f87b2cc2f3c77953db7 on September 8th 2020

* get_started
    - action_get_started
* thu_tuc
    - thutuc_form
    - form{"name":"thutuc_form"}
    - slot{"requested_slot":"don_vi"}
    - slot{"don_vi":"sở nội vụ"}
* chi_co_dv{"don_vi":"sở nội vụ"}
    - slot{"don_vi":"sở nội vụ"}
    - thutuc_form
    - slot{"don_vi":"sở nội vụ"}
* ten_thu_tuc
    - thutuc_form
    - form{"name":null}
    - slot{"tu_khoa":"thủ tục tặng danh hiệu chiến sĩ thi đua cấp tỉnh"}
    - action_thu_tuc
    - action_rsslot
    - slot{"key_tt":"156737"}
* show_thutuc{"key_tt":"156737"}
    - slot{"key_tt":"156737"}
    - action_show_thutuc
* bye
    - utter_bye
    - action_rsslot

## New Story

* thu_tuc
    - thutuc_form
    - form{"name":"thutuc_form"}
    - slot{"requested_slot":"don_vi"}
    - slot{"don_vi":"ubnd xã đại ân 1"}
* chi_co_dv{"don_vi":"ubnd xã đại ân 1"}
    - thutuc_form
    - slot{"don_vi":"xã đại ân 1"}
* ten_thu_tuc
    - thutuc_form
    - form{"name":null}
    - slot{"tu_khoa":"thủ tục đăng ký kết hôn"}
    - action_thu_tuc
    - action_rsslot
* ten_thu_tuc
    - thutuc_form
    - form{"name":"thutuc_form"}
    - slot{"requested_slot":"don_vi"}
    - slot{"don_vi":"sở công thương"}
* chi_co_dv{"don_vi":"sở công thương"}
    - thutuc_form
    - slot{"don_vi":"sở công thương"}

## New Story

* greet
    - action_greet
* thu_tuc
    - thutuc_form
    - form{"name":"thutuc_form"}
    - slot{"requested_slot":"don_vi"}
* greet
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_greet

## New Story

* greet
    - action_greet
* thu_tuc
    - thutuc_form
    - form{"name":"thutuc_form"}
    - slot{"requested_slot":"don_vi"}
* greet
    - action_deactivate_form
    - action_greet
    - utter_bye
* bye
	- utter_bye
    - action_rsslot
    - action_ss_started

##tra_cuu_hs_tccn

* tra_cuu_hs_tccn
  - tccn_form
  - form{"name": "tccn_form"}
  - form{"name": null}
  - action_tra_cuu_hs_tccn
  - action_rsslot
  - slot{"requested_slot": null}

## show ho so

* tra_cuu_hs_tccn
  - tccn_form
  - form{"name": "tccn_form"}
  - form{"name": null}
  - action_show_hoso
  - action_rsslot
  - slot{"requested_slot": null}