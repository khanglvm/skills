# Sources

Links to the material behind the Vietnamese layer, the cards and the linter. Nothing from these pages is copied here beyond short phrases quoted in the layers; license notes for the mined repositories are in `../ATTRIBUTION.md`. The cards refer to three groups by label: R1 (journalism and official style), R2 (technical, product and workplace Vietnamese) and R3 (AI-tell research and tools).

## Upstream

- blader/humanizer: https://github.com/blader/humanizer (pinned in `../UPSTREAM.json`)
- Wikipedia, "Signs of AI writing": https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## Mined repositories (MIT)

- cthpAiden/humanizer-vi: https://github.com/cthpAiden/humanizer-vi
- longhang2004/vietnamese-humanizer: https://github.com/longhang2004/vietnamese-humanizer
- cuongducle/viet-humanize: https://github.com/cuongducle/viet-humanize
- trussary/vietnamese-language-skill: https://github.com/trussary/vietnamese-language-skill
- haunguyendev/humanizer-vi: https://github.com/haunguyendev/humanizer-vi

## Style guides and official texts

- Microsoft Vietnamese Localization Style Guide: https://download.microsoft.com/download/b/f/e/bfecb1b4-21ab-48fd-a48c-c2471b026f8f/vie-vnm-StyleGuide.pdf
- Mozilla Firefox Vietnamese strings: https://github.com/mozilla-l10n/firefox-l10n
- Nghị định 30/2020/NĐ-CP (công tác văn thư): https://luatvietnam.vn/hanh-chinh/nghi-dinh-30-2020-nd-cp-ve-cong-tac-van-thu-moi-nhat-181212-d1.html, appendix at https://riam.edu.vn/nghi-dinh-ve-cong-tac-van-thu-phu-luc
- Quyết định 240/QĐ (1984), Bộ Giáo dục: https://thuvienphapluat.vn/van-ban/Giao-duc/Quyet-dinh-240-QD-nam-1984-chinh-ta-thuat-ngu-tieng-Viet-sach-giao-khoa-bao-van-ban-nganh-giao-duc-216818.aspx
- Luật Quảng cáo 16/2012/QH13, Điều 8 khoản 11 (as summarised in trussary/vietnamese-language-skill)

## R1: human news corpus

Fourteen articles published before November 2022, used for sentence and connector counts and for linter calibration. The texts are not in this repository.

- VnExpress: https://vnexpress.net/qua-roi-nam-2021-ky-la-4410513.html, https://vnexpress.net/anh-xe-om-mo-duong-cho-xe-cap-cuu-4143463.html, https://vnexpress.net/khoi-to-vu-an-lien-quan-viec-khai-tu-bo-me-chong-con-song-4327054.html
- Znews: https://znews.vn/khoi-to-vu-an-tron-ve-gia-dinh-vo-lam-lay-dich-covid-19-post1274600.html, https://znews.vn/de-nghi-ky-luat-7-can-bo-dien-trung-uong-quan-ly-nhieu-lanh-dao-dnnn-post1247408.html, https://znews.vn/gioi-tre-thu-trao-luu-vu-tru-du-doan-2022-post1288249.html
- VietNamNet: https://vietnamnet.vn/1-trieu-hoc-sinh-buoc-vao-ky-thi-tot-nghiep-thpt-2022-2036970.html
- Tuổi Trẻ: https://tuoitre.vn/nam-2021-khi-sach-cung-lao-dao-vi-covid-19-20211214193750204.htm, https://tuoitre.vn/thanh-tuu-y-khoa-2021-nhung-cong-hien-tu-chuyen-mon-va-y-duc-20220226213709978.htm, https://tuoitre.vn/nhin-lai-2021-2021122515344433.htm, https://tuoitre.vn/tuoi-tre-dang-gia-khi-biet-ban-than-muon-lam-gi-20210328213409921.htm, https://tuoitre.vn/tu-mot-comment-tren-tuoi-tre-online-den-khoan-nhuan-but-lon-nhat-cua-toi-2021112321365656.htm, https://tuoitre.vn/tri-thuc-tre-vi-giao-duc-2019-suc-song-sang-tao-tu-ban-tre-20191109090136624.htm
- Thanh Niên: https://thanhnien.vn/tam-chia-tay-sai-gon-ve-que-vi-covid-19-30-nam-muu-sinh-nuoc-mat-chay-dai-1851092116.htm, https://thanhnien.vn/cong-nhan-lo-mat-tet-khong-ve-que-mot-nam-tu-dung-thay-buon-1851028262.htm
- Lao Động: https://laodong.vn/cong-doan/cong-nhan-bat-an-khi-con-o-phong-tro-mot-minh-hoc-online-972220.ldo, https://laodong.vn/su-kien-binh-luan/nha-o-cho-cong-nhan-khong-the-chan-chu-966568.ldo
- Nhân Dân: https://nhandan.vn/thong-diep-manh-me-ve-xay-dung-chinh-don-dang-post668584.html

## R2: technical, product and workplace samples

- Tiki Engineering: https://medium.com/tiki-engineering/t%E1%BA%A1i-sao-tiki-ch%E1%BB%8Dn-react-native-51ce2a935861, https://medium.com/tiki-engineering/tiki-scale-in-10-years-225826296cb8, https://engineering.tiki.vn
- Viblo: https://viblo.asia/p/nhap-mon-cicd-voi-gitlab-07LKX9WPZV4, https://viblo.asia/q/MG24B0GELz3, https://viblo.asia/p/cach-don-gian-de-thuc-hien-mot-buoi-sprint-retrospective-aWj53B7Yl6m, https://viblo.asia/p/part-3-gerrit-code-review-with-jenkins-ci-tich-hop-ci-cd-eW65GYWOZDO
- Cybozu Vietnam, code review mindset: https://tech.cybozu.vn/7-code-review-mindset-giup-developer-di-duong-dai-tren-con-duong-lap-trinh-539bb
- toidicodedao: https://toidicodedao.com/tag/itviec
- Public issue threads and PRs: https://github.com/easywebhub/tasks/issues/90, https://github.com/easywebhub/tasks/issues/42, https://github.com/at-vunguyen/AT-FE-Training-Summer-2018-NguyenVanVu/pull/3, https://github.com/C0321G1/sprint2_backend_new/pull/4
- Firefox strings read: https://raw.githubusercontent.com/mozilla-l10n/firefox-l10n/main/vi/toolkit/toolkit/neterror/netError.ftl, https://raw.githubusercontent.com/mozilla-l10n/firefox-l10n/main/vi/browser/browser/preferences/preferences.ftl
- MoMo: https://momo.vn, https://www.momo.vn/hoi-dap/vi-sao-toi-thuc-hien-giao-dich-thanh-toan-khong-thanh-cong
- Shopee help centre: https://help.shopee.vn
- Base.vn release notes: https://help.base.vn/support/solutions/articles/63000288219-base-vn-c%E1%BA%ADp-nh%E1%BA%ADt-t%C3%ADnh-n%C4%83ng-th%C3%A1ng-1-2026
- Haravan release notes: https://hocvien.haravan.com/blogs/omnichannel/haravan-cap-nhat-tinh-nang-moi-thang-04-2026-late
- Agency landing page used as a boilerplate example: https://wow.com.vn/website-design

## R3: AI-tell research, tools and articles

- Cao Xuân Hạo, "Suy nghĩ về dịch thuật": https://www.caoxuan.com/article.php?Fl=archives%2Fcxhao_translation_doc
- Cao Xuân Hạo and Trần Thị Tuyết Mai, "Sổ tay sửa lỗi hành văn" (listing): https://archive.org/details/so-tay-sua-loi-hanh-van-loi-ngu-phap-trong-cau-co-trang-ngu-mo-dau-cao-xuan-hao-tran-thi-tuyet-mai
- Brands Vietnam, signs of AI-written content: https://help.brandsvietnam.com/vi/article/dau-hieu-nhan-biet-noi-dung-duoc-viet-boi-ai-3zy07d
- Phạm Mỹ, "Mùi AI", Báo Văn Nghệ: https://baovannghe.vn/mui-ai-26802.html
- Tân Phát Digital AI-text checker: https://tanphatdigital.com/vi/tools/kiem-tra-van-ban-ai
- Upcontent: https://upcontent.vn/kiem-tra-van-ban-ai/
- Finhay prompt guide: https://www.finhay.com.vn/meo-dung-chatgpt-khong-bi-van-mau-robotic
- Nghiện AI group post on social-post tells: https://www.facebook.com/groups/aiartworksvn/posts/4450406765172173
- VnExpress summary of critiques of AI prose: https://vnexpress.net/van-chuong-ai-hoa-my-nhung-rong-tuech-5128963.html
- ViDetect (Tran et al., 2024): https://arxiv.org/abs/2405.03206
- Stylometry of LLM text: https://arxiv.org/pdf/2507.00838
- Lâm Minh Hoa, on *bị* and the Vietnamese passive: https://dulieu.itrithuc.vn/media/dataset/2020_08/ky_05740.pdf
- VNU papers on passive translation and nominalisation: http://vci.vnu.edu.vn/upload/15022/pdf/5763a1817f8b9aa7b58b45d2.pdf, http://vci.vnu.edu.vn/upload/15022/pdf/576383c67f8b9a384b8b45f1.pdf
- Other tools reviewed and not used: https://github.com/ContextBoxAI/vi-humanizer, https://skills.rest/skill/viet-ai-humanizer, https://github.com/vutuongvy101/multilingual-ai-human-text-detection
