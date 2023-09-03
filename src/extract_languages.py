from bs4 import BeautifulSoup as Soup
from src.language import Language
from src.extractworld import saveToJson

text = """
<table>
    <tbody><tr><th>Country</th><th>Language</th><th>Two Letter</th><th>Three Letter </th><th>Number (LCID)</th></tr>
    <tr><td>Afghanistan</td><td>Pashto</td><td>ps-AF</td><td>ps-AFG</td><td>1123</td></tr>
    <tr><td>Afghanistan</td><td>Persian</td><td>fa-AF</td><td>fa-AFG</td><td>4096</td></tr>
    <tr><td>Afghanistan</td><td>Uzbek</td><td>uz-AF</td><td>uz-AFG</td><td>4096</td></tr>
    <tr><td>Åland Islands</td><td>Swedish</td><td>sv-AX</td><td>sv-ALA</td><td>4096</td></tr>
    <tr><td>Albania</td><td>Albanian</td><td>sq-AL</td><td>sq-ALB</td><td>1052</td></tr>
    <tr><td>Albania</td><td>English</td><td>en-AL</td><td>en-ALB</td><td>4096</td></tr>
    <tr><td>Algeria</td><td>Arabic</td><td>ar-DZ</td><td>ar-DZA</td><td>5121</td></tr>
    <tr><td>Algeria</td><td>French</td><td>fr-DZ</td><td>fr-DZA</td><td>4096</td></tr>
    <tr><td>Algeria</td><td>Kabyle</td><td>kab-DZ</td><td>kab-DZA</td><td>4096</td></tr>
    <tr><td>American Samoa</td><td>English</td><td>en-AS</td><td>en-ASM</td><td>4096</td></tr>
    <tr><td>Andorra</td><td>Catalan</td><td>ca-AD</td><td>ca-AND</td><td>4096</td></tr>
    <tr><td>Andorra</td><td>English</td><td>en-AD</td><td>en-AND</td><td>4096</td></tr>
    <tr><td>Angola</td><td>Lingala</td><td>ln-AO</td><td>ln-AGO</td><td>4096</td></tr>
    <tr><td>Angola</td><td>Portuguese</td><td>pt-AO</td><td>pt-AGO</td><td>4096</td></tr>
    <tr><td>Anguilla</td><td>English</td><td>en-AI</td><td>en-AIA</td><td>4096</td></tr>
    <tr><td>Anguilla</td><td>Spanish</td><td>es-AI</td><td>es-AIA</td><td>4096</td></tr>
    <tr><td>Antigua &amp; Barbuda</td><td>English</td><td>en-AG</td><td>en-ATG</td><td>4096</td></tr>
    <tr><td>Antigua &amp; Barbuda</td><td>Spanish</td><td>es-AG</td><td>es-ATG</td><td>4096</td></tr>
    <tr><td>Argentina</td><td>English</td><td>en-AR</td><td>en-ARG</td><td>4096</td></tr>
    <tr><td>Argentina</td><td>Spanish</td><td>es-AR</td><td>es-ARG</td><td>11274</td></tr>
    <tr><td>Armenia</td><td>Armenian</td><td>hy-AM</td><td>hy-ARM</td><td>1067</td></tr>
    <tr><td>Aruba</td><td>Dutch</td><td>nl-AW</td><td>nl-ABW</td><td>4096</td></tr>
    <tr><td>Aruba</td><td>Spanish</td><td>es-AW</td><td>es-ABW</td><td>4096</td></tr>
    <tr><td>Australia</td><td>English</td><td>en-AU</td><td>en-AUS</td><td>3081</td></tr>
    <tr><td>Austria</td><td>English</td><td>en-AT</td><td>en-AUT</td><td>4096</td></tr>
    <tr><td>Austria</td><td>German</td><td>de-AT</td><td>de-AUT</td><td>3079</td></tr>
    <tr><td>Azerbaijan</td><td>Azerbaijani</td><td>az-AZ</td><td>az-AZE</td><td>1068</td></tr>
    <tr><td>Azerbaijan</td><td>Azerbaijani</td><td>az-AZ</td><td>az-AZE</td><td>2092</td></tr>
    <tr><td>Bahamas</td><td>English</td><td>en-BS</td><td>en-BHS</td><td>4096</td></tr>
    <tr><td>Bahamas</td><td>Spanish</td><td>es-BS</td><td>es-BHS</td><td>4096</td></tr>
    <tr><td>Bahrain</td><td>Arabic</td><td>ar-BH</td><td>ar-BHR</td><td>15361</td></tr>
    <tr><td>Bangladesh</td><td>Bangla</td><td>bn-BD</td><td>bn-BGD</td><td>2117</td></tr>
    <tr><td>Bangladesh</td><td>Chakma</td><td>ccp-BD</td><td>ccp-BGD</td><td>4096</td></tr>
    <tr><td>Bangladesh</td><td>English</td><td>en-BD</td><td>en-BGD</td><td>4096</td></tr>
    <tr><td>Barbados</td><td>English</td><td>en-BB</td><td>en-BRB</td><td>4096</td></tr>
    <tr><td>Barbados</td><td>Spanish</td><td>es-BB</td><td>es-BRB</td><td>4096</td></tr>
    <tr><td>Belarus</td><td>Belarusian</td><td>be-BY</td><td>be-BLR</td><td>1059</td></tr>
    <tr><td>Belarus</td><td>Russian</td><td>ru-BY</td><td>ru-BLR</td><td>4096</td></tr>
    <tr><td>Belgium</td><td>Dutch</td><td>nl-BE</td><td>nl-BEL</td><td>2067</td></tr>
    <tr><td>Belgium</td><td>English</td><td>en-BE</td><td>en-BEL</td><td>4096</td></tr>
    <tr><td>Belgium</td><td>French</td><td>fr-BE</td><td>fr-BEL</td><td>2060</td></tr>
    <tr><td>Belgium</td><td>German</td><td>de-BE</td><td>de-BEL</td><td>4096</td></tr>
    <tr><td>Belgium</td><td>Walloon</td><td>wa-BE</td><td>wa-BEL</td><td>4096</td></tr>
    <tr><td>Belize</td><td>English</td><td>en-BZ</td><td>en-BLZ</td><td>10249</td></tr>
    <tr><td>Belize</td><td>Spanish</td><td>es-BZ</td><td>es-BLZ</td><td>4096</td></tr>
    <tr><td>Benin</td><td>French</td><td>fr-BJ</td><td>fr-BEN</td><td>4096</td></tr>
    <tr><td>Benin</td><td>Yoruba</td><td>yo-BJ</td><td>yo-BEN</td><td>4096</td></tr>
    <tr><td>Bermuda</td><td>English</td><td>en-BM</td><td>en-BMU</td><td>4096</td></tr>
    <tr><td>Bermuda</td><td>Spanish</td><td>es-BM</td><td>es-BMU</td><td>4096</td></tr>
    <tr><td>Bhutan</td><td>Dzongkha</td><td>dz-BT</td><td>dz-BTN</td><td>3153</td></tr>
    <tr><td>Bolivia</td><td>Quechua</td><td>qu-BO</td><td>qu-BOL</td><td>4096</td></tr>
    <tr><td>Bolivia</td><td>Spanish</td><td>es-BO</td><td>es-BOL</td><td>16394</td></tr>
    <tr><td>Bosnia &amp; Herzegovina</td><td>Bosnian</td><td>bs-BA</td><td>bs-BIH</td><td>5146</td></tr>
    <tr><td>Bosnia &amp; Herzegovina</td><td>Bosnian</td><td>bs-BA</td><td>bs-BIH</td><td>8218</td></tr>
    <tr><td>Bosnia &amp; Herzegovina</td><td>Croatian</td><td>hr-BA</td><td>hr-BIH</td><td>4122</td></tr>
    <tr><td>Bosnia &amp; Herzegovina</td><td>English</td><td>en-BA</td><td>en-BIH</td><td>4096</td></tr>
    <tr><td>Bosnia &amp; Herzegovina</td><td>Serbian</td><td>sr-BA</td><td>sr-BIH</td><td>6170</td></tr>
    <tr><td>Bosnia &amp; Herzegovina</td><td>Serbian</td><td>sr-BA</td><td>sr-BIH</td><td>7194</td></tr>
    <tr><td>Botswana</td><td>English</td><td>en-BW</td><td>en-BWA</td><td>4096</td></tr>
    <tr><td>Botswana</td><td>Tswana</td><td>tn-BW</td><td>tn-BWA</td><td>2098</td></tr>
    <tr><td>Brazil</td><td>English</td><td>en-BR</td><td>en-BRA</td><td>4096</td></tr>
    <tr><td>Brazil</td><td>Portuguese</td><td>pt-BR</td><td>pt-BRA</td><td>1046</td></tr>
    <tr><td>Brazil</td><td>Spanish</td><td>es-BR</td><td>es-BRA</td><td>4096</td></tr>
    <tr><td>British Indian Ocean Territory</td><td>English</td><td>en-IO</td><td>en-IOT</td><td>4096</td></tr>
    <tr><td>British Virgin Islands</td><td>English</td><td>en-VG</td><td>en-VGB</td><td>4096</td></tr>
    <tr><td>British Virgin Islands</td><td>Spanish</td><td>es-VG</td><td>es-VGB</td><td>4096</td></tr>
    <tr><td>Brunei</td><td>Malay</td><td>ms-BN</td><td>ms-BRN</td><td>2110</td></tr>
    <tr><td>Brunei</td><td>Malay</td><td>ms-BN</td><td>ms-BRN</td><td>4096</td></tr>
    <tr><td>Bulgaria</td><td>Bulgarian</td><td>bg-BG</td><td>bg-BGR</td><td>1026</td></tr>
    <tr><td>Bulgaria</td><td>English</td><td>en-BG</td><td>en-BGR</td><td>4096</td></tr>
    <tr><td>Burkina Faso</td><td>French</td><td>fr-BF</td><td>fr-BFA</td><td>4096</td></tr>
    <tr><td>Burkina Faso</td><td>Fulah</td><td>ff-BF</td><td>ff-BFA</td><td>4096</td></tr>
    <tr><td>Burundi</td><td>English</td><td>en-BI</td><td>en-BDI</td><td>4096</td></tr>
    <tr><td>Burundi</td><td>French</td><td>fr-BI</td><td>fr-BDI</td><td>4096</td></tr>
    <tr><td>Burundi</td><td>Rundi</td><td>rn-BI</td><td>rn-BDI</td><td>4096</td></tr>
    <tr><td>Cambodia</td><td>Khmer</td><td>km-KH</td><td>km-KHM</td><td>1107</td></tr>
    <tr><td>Cameroon</td><td>Aghem</td><td>agq-CM</td><td>agq-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Bafia</td><td>ksf-CM</td><td>ksf-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Basaa</td><td>bas-CM</td><td>bas-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Duala</td><td>dua-CM</td><td>dua-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>English</td><td>en-CM</td><td>en-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Ewondo</td><td>ewo-CM</td><td>ewo-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>French</td><td>fr-CM</td><td>fr-CMR</td><td>11276</td></tr>
    <tr><td>Cameroon</td><td>Fulah</td><td>ff-CM</td><td>ff-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Kako</td><td>kkj-CM</td><td>kkj-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Kwasio</td><td>nmg-CM</td><td>nmg-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Metaʼ</td><td>mgo-CM</td><td>mgo-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Mundang</td><td>mua-CM</td><td>mua-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Ngiemboon</td><td>nnh-CM</td><td>nnh-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Ngomba</td><td>jgo-CM</td><td>jgo-CMR</td><td>4096</td></tr>
    <tr><td>Cameroon</td><td>Yangben</td><td>yav-CM</td><td>yav-CMR</td><td>4096</td></tr>
    <tr><td>Canada</td><td>English</td><td>en-CA</td><td>en-CAN</td><td>4105</td></tr>
    <tr><td>Canada</td><td>French</td><td>fr-CA</td><td>fr-CAN</td><td>3084</td></tr>
    <tr><td>Canada</td><td>Inuktitut</td><td>iu-CA</td><td>iu-CAN</td><td>4096</td></tr>
    <tr><td>Canada</td><td>Mohawk</td><td>moh-CA</td><td>moh-CAN</td><td>1148</td></tr>
    <tr><td>Canada</td><td>Spanish</td><td>es-CA</td><td>es-CAN</td><td>4096</td></tr>
    <tr><td>Canary Islands</td><td>Spanish</td><td>es-IC</td><td>es-IC </td><td>4096</td></tr>
    <tr><td>Cape Verde</td><td>Kabuverdianu</td><td>kea-CV</td><td>kea-CPV</td><td>4096</td></tr>
    <tr><td>Cape Verde</td><td>Portuguese</td><td>pt-CV</td><td>pt-CPV</td><td>4096</td></tr>
    <tr><td>Caribbean Netherlands</td><td>Dutch</td><td>nl-BQ</td><td>nl-BES</td><td>4096</td></tr>
    <tr><td>Caribbean Netherlands</td><td>Spanish</td><td>es-BQ</td><td>es-BES</td><td>4096</td></tr>
    <tr><td>Cayman Islands</td><td>English</td><td>en-KY</td><td>en-CYM</td><td>4096</td></tr>
    <tr><td>Cayman Islands</td><td>Spanish</td><td>es-KY</td><td>es-CYM</td><td>4096</td></tr>
    <tr><td>Central African Republic</td><td>French</td><td>fr-CF</td><td>fr-CAF</td><td>4096</td></tr>
    <tr><td>Central African Republic</td><td>Lingala</td><td>ln-CF</td><td>ln-CAF</td><td>4096</td></tr>
    <tr><td>Central African Republic</td><td>Sango</td><td>sg-CF</td><td>sg-CAF</td><td>4096</td></tr>
    <tr><td>Ceuta &amp; Melilla</td><td>Spanish</td><td>es-EA</td><td>es-EA </td><td>4096</td></tr>
    <tr><td>Chad</td><td>Arabic</td><td>ar-TD</td><td>ar-TCD</td><td>4096</td></tr>
    <tr><td>Chad</td><td>French</td><td>fr-TD</td><td>fr-TCD</td><td>4096</td></tr>
    <tr><td>Chile</td><td>English</td><td>en-CL</td><td>en-CHL</td><td>4096</td></tr>
    <tr><td>Chile</td><td>Mapuche</td><td>arn-CL</td><td>arn-CHL</td><td>1146</td></tr>
    <tr><td>Chile</td><td>Spanish</td><td>es-CL</td><td>es-CHL</td><td>13322</td></tr>
    <tr><td>China mainland</td><td>Cantonese</td><td>yue-CN</td><td>yue-CHN</td><td>4096</td></tr>
    <tr><td>China mainland</td><td>Chinese</td><td>zh-CN</td><td>zh-CHN</td><td>4096</td></tr>
    <tr><td>China mainland</td><td>Chinese</td><td>zh-CN</td><td>zh-CHN</td><td>4096</td></tr>
    <tr><td>China mainland</td><td>English</td><td>en-CN</td><td>en-CHN</td><td>4096</td></tr>
    <tr><td>China mainland</td><td>Sichuan Yi</td><td>ii-CN</td><td>ii-CHN</td><td>1144</td></tr>
    <tr><td>China mainland</td><td>Tibetan</td><td>bo-CN</td><td>bo-CHN</td><td>1105</td></tr>
    <tr><td>China mainland</td><td>Uyghur</td><td>ug-CN</td><td>ug-CHN</td><td>1152</td></tr>
    <tr><td>Christmas Island</td><td>English</td><td>en-CX</td><td>en-CXR</td><td>4096</td></tr>
    <tr><td>Cocos (Keeling) Islands</td><td>English</td><td>en-CC</td><td>en-CCK</td><td>4096</td></tr>
    <tr><td>Colombia</td><td>English</td><td>en-CO</td><td>en-COL</td><td>4096</td></tr>
    <tr><td>Colombia</td><td>Spanish</td><td>es-CO</td><td>es-COL</td><td>9226</td></tr>
    <tr><td>Comoros</td><td>Arabic</td><td>ar-KM</td><td>ar-COM</td><td>4096</td></tr>
    <tr><td>Comoros</td><td>French</td><td>fr-KM</td><td>fr-COM</td><td>4096</td></tr>
    <tr><td>Congo - Brazzaville</td><td>French</td><td>fr-CG</td><td>fr-COG</td><td>4096</td></tr>
    <tr><td>Congo - Brazzaville</td><td>Lingala</td><td>ln-CG</td><td>ln-COG</td><td>4096</td></tr>
    <tr><td>Congo - Kinshasa</td><td>French</td><td>fr-CD</td><td>fr-COD</td><td>9228</td></tr>
    <tr><td>Congo - Kinshasa</td><td>Lingala</td><td>ln-CD</td><td>ln-COD</td><td>4096</td></tr>
    <tr><td>Congo - Kinshasa</td><td>Luba-Katanga</td><td>lu-CD</td><td>lu-COD</td><td>4096</td></tr>
    <tr><td>Congo - Kinshasa</td><td>Swahili</td><td>sw-CD</td><td>sw-COD</td><td>4096</td></tr>
    <tr><td>Cook Islands</td><td>English</td><td>en-CK</td><td>en-COK</td><td>4096</td></tr>
    <tr><td>Costa Rica</td><td>Spanish</td><td>es-CR</td><td>es-CRI</td><td>5130</td></tr>
    <tr><td>Côte d’Ivoire</td><td>French</td><td>fr-CI</td><td>fr-CIV</td><td>12300</td></tr>
    <tr><td>Croatia</td><td>Croatian</td><td>hr-HR</td><td>hr-HRV</td><td>1050</td></tr>
    <tr><td>Croatia</td><td>English</td><td>en-HR</td><td>en-HRV</td><td>4096</td></tr>
    <tr><td>Cuba</td><td>Spanish</td><td>es-CU</td><td>es-CUB</td><td>23562</td></tr>
    <tr><td>Curaçao</td><td>Dutch</td><td>nl-CW</td><td>nl-CUW</td><td>4096</td></tr>
    <tr><td>Curaçao</td><td>Spanish</td><td>es-CW</td><td>es-CUW</td><td>4096</td></tr>
    <tr><td>Cyprus</td><td>English</td><td>en-CY</td><td>en-CYP</td><td>4096</td></tr>
    <tr><td>Cyprus</td><td>Greek</td><td>el-CY</td><td>el-CYP</td><td>4096</td></tr>
    <tr><td>Cyprus</td><td>Turkish</td><td>tr-CY</td><td>tr-CYP</td><td>4096</td></tr>
    <tr><td>Czechia</td><td>Czech</td><td>cs-CZ</td><td>cs-CZE</td><td>1029</td></tr>
    <tr><td>Czechia</td><td>English</td><td>en-CZ</td><td>en-CZE</td><td>4096</td></tr>
    <tr><td>Denmark</td><td>Danish</td><td>da-DK</td><td>da-DNK</td><td>1030</td></tr>
    <tr><td>Denmark</td><td>English</td><td>en-DK</td><td>en-DNK</td><td>4096</td></tr>
    <tr><td>Denmark</td><td>Faroese</td><td>fo-DK</td><td>fo-DNK</td><td>4096</td></tr>
    <tr><td>Diego Garcia</td><td>English</td><td>en-DG</td><td>en-DGA</td><td>4096</td></tr>
    <tr><td>Djibouti</td><td>Arabic</td><td>ar-DJ</td><td>ar-DJI</td><td>4096</td></tr>
    <tr><td>Djibouti</td><td>French</td><td>fr-DJ</td><td>fr-DJI</td><td>4096</td></tr>
    <tr><td>Djibouti</td><td>Somali</td><td>so-DJ</td><td>so-DJI</td><td>4096</td></tr>
    <tr><td>Dominica</td><td>English</td><td>en-DM</td><td>en-DMA</td><td>4096</td></tr>
    <tr><td>Dominica</td><td>Spanish</td><td>es-DM</td><td>es-DMA</td><td>4096</td></tr>
    <tr><td>Dominican Republic</td><td>Spanish</td><td>es-DO</td><td>es-DOM</td><td>7178</td></tr>
    <tr><td>Ecuador</td><td>Quechua</td><td>qu-EC</td><td>qu-ECU</td><td>4096</td></tr>
    <tr><td>Ecuador</td><td>Spanish</td><td>es-EC</td><td>es-ECU</td><td>12298</td></tr>
    <tr><td>Egypt</td><td>Arabic</td><td>ar-EG</td><td>ar-EGY</td><td>3073</td></tr>
    <tr><td>El Salvador</td><td>Spanish</td><td>es-SV</td><td>es-SLV</td><td>17418</td></tr>
    <tr><td>Equatorial Guinea</td><td>French</td><td>fr-GQ</td><td>fr-GNQ</td><td>4096</td></tr>
    <tr><td>Equatorial Guinea</td><td>Portuguese</td><td>pt-GQ</td><td>pt-GNQ</td><td>4096</td></tr>
    <tr><td>Equatorial Guinea</td><td>Spanish</td><td>es-GQ</td><td>es-GNQ</td><td>4096</td></tr>
    <tr><td>Eritrea</td><td>Arabic</td><td>ar-ER</td><td>ar-ERI</td><td>4096</td></tr>
    <tr><td>Eritrea</td><td>Blin</td><td>byn-ER</td><td>byn-ERI</td><td>4096</td></tr>
    <tr><td>Eritrea</td><td>English</td><td>en-ER</td><td>en-ERI</td><td>4096</td></tr>
    <tr><td>Eritrea</td><td>Geez</td><td>gez-ER</td><td>gez-ERI</td><td>4096</td></tr>
    <tr><td>Eritrea</td><td>Tigre</td><td>tig-ER</td><td>tig-ERI</td><td>4096</td></tr>
    <tr><td>Eritrea</td><td>Tigrinya</td><td>ti-ER</td><td>ti-ERI</td><td>2163</td></tr>
    <tr><td>Estonia</td><td>English</td><td>en-EE</td><td>en-EST</td><td>4096</td></tr>
    <tr><td>Estonia</td><td>Estonian</td><td>et-EE</td><td>et-EST</td><td>1061</td></tr>
    <tr><td>Eswatini</td><td>English</td><td>en-SZ</td><td>en-SWZ</td><td>4096</td></tr>
    <tr><td>Eswatini</td><td>Swati</td><td>ss-SZ</td><td>ss-SWZ</td><td>4096</td></tr>
    <tr><td>Ethiopia</td><td>Amharic</td><td>am-ET</td><td>am-ETH</td><td>1118</td></tr>
    <tr><td>Ethiopia</td><td>Geez</td><td>gez-ET</td><td>gez-ETH</td><td>4096</td></tr>
    <tr><td>Ethiopia</td><td>Oromo</td><td>om-ET</td><td>om-ETH</td><td>1138</td></tr>
    <tr><td>Ethiopia</td><td>Somali</td><td>so-ET</td><td>so-ETH</td><td>4096</td></tr>
    <tr><td>Ethiopia</td><td>Tigrinya</td><td>ti-ET</td><td>ti-ETH</td><td>1139</td></tr>
    <tr><td>Ethiopia</td><td>Wolaytta</td><td>wal-ET</td><td>wal-ETH</td><td>4096</td></tr>
    <tr><td>Europe</td><td>English</td><td>en-150</td><td>en-</td><td>4096</td></tr>
    <tr><td>Falkland Islands</td><td>English</td><td>en-FK</td><td>en-FLK</td><td>4096</td></tr>
    <tr><td>Falkland Islands</td><td>Spanish</td><td>es-FK</td><td>es-FLK</td><td>4096</td></tr>
    <tr><td>Faroe Islands</td><td>Faroese</td><td>fo-FO</td><td>fo-FRO</td><td>1080</td></tr>
    <tr><td>Fiji</td><td>English</td><td>en-FJ</td><td>en-FJI</td><td>4096</td></tr>
    <tr><td>Finland</td><td>English</td><td>en-FI</td><td>en-FIN</td><td>4096</td></tr>
    <tr><td>Finland</td><td>Finnish</td><td>fi-FI</td><td>fi-FIN</td><td>1035</td></tr>
    <tr><td>Finland</td><td>Inari Sami</td><td>smn-FI</td><td>smn-FIN</td><td>9275</td></tr>
    <tr><td>Finland</td><td>Northern Sami</td><td>se-FI</td><td>se-FIN</td><td>3131</td></tr>
    <tr><td>Finland</td><td>Swedish</td><td>sv-FI</td><td>sv-FIN</td><td>2077</td></tr>
    <tr><td>France</td><td>Breton</td><td>br-FR</td><td>br-FRA</td><td>1150</td></tr>
    <tr><td>France</td><td>Catalan</td><td>ca-FR</td><td>ca-FRA</td><td>4096</td></tr>
    <tr><td>France</td><td>Corsican</td><td>co-FR</td><td>co-FRA</td><td>1155</td></tr>
    <tr><td>France</td><td>English</td><td>en-FR</td><td>en-FRA</td><td>4096</td></tr>
    <tr><td>France</td><td>French</td><td>fr-FR</td><td>fr-FRA</td><td>1036</td></tr>
    <tr><td>France</td><td>Occitan</td><td>oc-FR</td><td>oc-FRA</td><td>1154</td></tr>
    <tr><td>France</td><td>Portuguese</td><td>pt-FR</td><td>pt-FRA</td><td>4096</td></tr>
    <tr><td>France</td><td>Swiss German</td><td>gsw-FR</td><td>gsw-FRA</td><td>1156</td></tr>
    <tr><td>French Guiana</td><td>French</td><td>fr-GF</td><td>fr-GUF</td><td>4096</td></tr>
    <tr><td>French Guiana</td><td>Spanish</td><td>es-GF</td><td>es-GUF</td><td>4096</td></tr>
    <tr><td>French Polynesia</td><td>French</td><td>fr-PF</td><td>fr-PYF</td><td>4096</td></tr>
    <tr><td>Gabon</td><td>French</td><td>fr-GA</td><td>fr-GAB</td><td>4096</td></tr>
    <tr><td>Gambia</td><td>English</td><td>en-GM</td><td>en-GMB</td><td>4096</td></tr>
    <tr><td>Gambia</td><td>Fulah</td><td>ff-GM</td><td>ff-GMB</td><td>4096</td></tr>
    <tr><td>Georgia</td><td>Georgian</td><td>ka-GE</td><td>ka-GEO</td><td>1079</td></tr>
    <tr><td>Georgia</td><td>Ossetic</td><td>os-GE</td><td>os-GEO</td><td>4096</td></tr>
    <tr><td>Germany</td><td>Colognian</td><td>ksh-DE</td><td>ksh-DEU</td><td>4096</td></tr>
    <tr><td>Germany</td><td>English</td><td>en-DE</td><td>en-DEU</td><td>4096</td></tr>
    <tr><td>Germany</td><td>German</td><td>de-DE</td><td>de-DEU</td><td>1031</td></tr>
    <tr><td>Germany</td><td>Low German</td><td>nds-DE</td><td>nds-DEU</td><td>4096</td></tr>
    <tr><td>Germany</td><td>Lower Sorbian</td><td>dsb-DE</td><td>dsb-DEU</td><td>2094</td></tr>
    <tr><td>Germany</td><td>Upper Sorbian</td><td>hsb-DE</td><td>hsb-DEU</td><td>1070</td></tr>
    <tr><td>Ghana</td><td>Akan</td><td>ak-GH</td><td>ak-GHA</td><td>4096</td></tr>
    <tr><td>Ghana</td><td>English</td><td>en-GH</td><td>en-GHA</td><td>4096</td></tr>
    <tr><td>Ghana</td><td>Ewe</td><td>ee-GH</td><td>ee-GHA</td><td>4096</td></tr>
    <tr><td>Ghana</td><td>Fulah</td><td>ff-GH</td><td>ff-GHA</td><td>4096</td></tr>
    <tr><td>Ghana</td><td>Ga</td><td>gaa-GH</td><td>gaa-GHA</td><td>4096</td></tr>
    <tr><td>Ghana</td><td>Hausa</td><td>ha-GH</td><td>ha-GHA</td><td>4096</td></tr>
    <tr><td>Gibraltar</td><td>English</td><td>en-GI</td><td>en-GIB</td><td>4096</td></tr>
    <tr><td>Greece</td><td>English</td><td>en-GR</td><td>en-GRC</td><td>4096</td></tr>
    <tr><td>Greece</td><td>Greek</td><td>el-GR</td><td>el-GRC</td><td>1032</td></tr>
    <tr><td>Greenland</td><td>Danish</td><td>da-GL</td><td>da-GRL</td><td>4096</td></tr>
    <tr><td>Greenland</td><td>Kalaallisut</td><td>kl-GL</td><td>kl-GRL</td><td>1135</td></tr>
    <tr><td>Greenland</td><td>Spanish</td><td>es-GL</td><td>es-GRL</td><td>4096</td></tr>
    <tr><td>Grenada</td><td>English</td><td>en-GD</td><td>en-GRD</td><td>4096</td></tr>
    <tr><td>Grenada</td><td>Spanish</td><td>es-GD</td><td>es-GRD</td><td>4096</td></tr>
    <tr><td>Guadeloupe</td><td>French</td><td>fr-GP</td><td>fr-GLP</td><td>4096</td></tr>
    <tr><td>Guadeloupe</td><td>Spanish</td><td>es-GP</td><td>es-GLP</td><td>4096</td></tr>
    <tr><td>Guam</td><td>English</td><td>en-GU</td><td>en-GUM</td><td>4096</td></tr>
    <tr><td>Guatemala</td><td>Spanish</td><td>es-GT</td><td>es-GTM</td><td>4106</td></tr>
    <tr><td>Guernsey</td><td>English</td><td>en-GG</td><td>en-GGY</td><td>4096</td></tr>
    <tr><td>Guinea-Bissau</td><td>Fulah</td><td>ff-GW</td><td>ff-GNB</td><td>4096</td></tr>
    <tr><td>Guinea-Bissau</td><td>Portuguese</td><td>pt-GW</td><td>pt-GNB</td><td>4096</td></tr>
    <tr><td>Guinea</td><td>French</td><td>fr-GN</td><td>fr-GIN</td><td>4096</td></tr>
    <tr><td>Guinea</td><td>Fulah</td><td>ff-GN</td><td>ff-GIN</td><td>4096</td></tr>
    <tr><td>Guinea</td><td>Kpelle</td><td>kpe-GN</td><td>kpe-GIN</td><td>4096</td></tr>
    <tr><td>Guinea</td><td>N’Ko</td><td>nqo-GN</td><td>nqo-GIN</td><td>4096</td></tr>
    <tr><td>Guyana</td><td>English</td><td>en-GY</td><td>en-GUY</td><td>4096</td></tr>
    <tr><td>Guyana</td><td>Spanish</td><td>es-GY</td><td>es-GUY</td><td>4096</td></tr>
    <tr><td>Haiti</td><td>French</td><td>fr-HT</td><td>fr-HTI</td><td>15372</td></tr>
    <tr><td>Haiti</td><td>Spanish</td><td>es-HT</td><td>es-HTI</td><td>4096</td></tr>
    <tr><td>Honduras</td><td>Spanish</td><td>es-HN</td><td>es-HND</td><td>18442</td></tr>
    <tr><td>Hong Kong</td><td>Cantonese</td><td>yue-HK</td><td>yue-HKG</td><td>4096</td></tr>
    <tr><td>Hong Kong</td><td>Chinese</td><td>zh-HK</td><td>zh-HKG</td><td>4096</td></tr>
    <tr><td>Hong Kong</td><td>Chinese</td><td>zh-HK</td><td>zh-HKG</td><td>4096</td></tr>
    <tr><td>Hong Kong</td><td>English</td><td>en-HK</td><td>en-HKG</td><td>15369</td></tr>
    <tr><td>Hungary</td><td>English</td><td>en-HU</td><td>en-HUN</td><td>4096</td></tr>
    <tr><td>Hungary</td><td>Hungarian</td><td>hu-HU</td><td>hu-HUN</td><td>1038</td></tr>
    <tr><td>Iceland</td><td>English</td><td>en-IS</td><td>en-ISL</td><td>4096</td></tr>
    <tr><td>Iceland</td><td>Icelandic</td><td>is-IS</td><td>is-ISL</td><td>1039</td></tr>
    <tr><td>India</td><td>Assamese</td><td>as-IN</td><td>as-IND</td><td>1101</td></tr>
    <tr><td>India</td><td>Bangla</td><td>bn-IN</td><td>bn-IND</td><td>1093</td></tr>
    <tr><td>India</td><td>Bodo</td><td>brx-IN</td><td>brx-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Chakma</td><td>ccp-IN</td><td>ccp-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>English</td><td>en-IN</td><td>en-IND</td><td>16393</td></tr>
    <tr><td>India</td><td>Gujarati</td><td>gu-IN</td><td>gu-IND</td><td>1095</td></tr>
    <tr><td>India</td><td>Hindi</td><td>hi-IN</td><td>hi-IND</td><td>1081</td></tr>
    <tr><td>India</td><td>Kannada</td><td>kn-IN</td><td>kn-IND</td><td>1099</td></tr>
    <tr><td>India</td><td>Kashmiri</td><td>ks-IN</td><td>ks-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Kashmiri</td><td>ks-IN</td><td>ks-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Kashmiri</td><td>ks-IN</td><td>ks-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Konkani</td><td>kok-IN</td><td>kok-IND</td><td>1111</td></tr>
    <tr><td>India</td><td>Malayalam</td><td>ml-IN</td><td>ml-IND</td><td>1100</td></tr>
    <tr><td>India</td><td>Manipuri</td><td>mni-IN</td><td>mni-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Manipuri</td><td>mni-IN</td><td>mni-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Marathi</td><td>mr-IN</td><td>mr-IND</td><td>1102</td></tr>
    <tr><td>India</td><td>Nepali</td><td>ne-IN</td><td>ne-IND</td><td>2145</td></tr>
    <tr><td>India</td><td>Odia</td><td>or-IN</td><td>or-IND</td><td>1096</td></tr>
    <tr><td>India</td><td>Punjabi</td><td>pa-IN</td><td>pa-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Sanskrit</td><td>sa-IN</td><td>sa-IND</td><td>1103</td></tr>
    <tr><td>India</td><td>Santali</td><td>sat-IN</td><td>sat-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Santali</td><td>sat-IN</td><td>sat-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Tamil</td><td>ta-IN</td><td>ta-IND</td><td>1097</td></tr>
    <tr><td>India</td><td>Telugu</td><td>te-IN</td><td>te-IND</td><td>1098</td></tr>
    <tr><td>India</td><td>Tibetan</td><td>bo-IN</td><td>bo-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Urdu</td><td>ur-IN</td><td>ur-IND</td><td>2080</td></tr>
    <tr><td>India</td><td>Urdu</td><td>ur-IN</td><td>ur-IND</td><td>4096</td></tr>
    <tr><td>India</td><td>Urdu</td><td>ur-IN</td><td>ur-IND</td><td>4096</td></tr>
    <tr><td>Indonesia</td><td>English</td><td>en-ID</td><td>en-IDN</td><td>14345</td></tr>
    <tr><td>Indonesia</td><td>Indonesian</td><td>id-ID</td><td>id-IDN</td><td>1057</td></tr>
    <tr><td>Indonesia</td><td>Javanese</td><td>jv-ID</td><td>jv-IDN</td><td>4096</td></tr>
    <tr><td>Iran</td><td>Kurdish, Sorani</td><td>ckb-IR</td><td>ckb-IRN</td><td>4096</td></tr>
    <tr><td>Iran</td><td>Mazanderani</td><td>mzn-IR</td><td>mzn-IRN</td><td>4096</td></tr>
    <tr><td>Iran</td><td>Northern Luri</td><td>lrc-IR</td><td>lrc-IRN</td><td>4096</td></tr>
    <tr><td>Iran</td><td>Persian</td><td>fa-IR</td><td>fa-IRN</td><td>1065</td></tr>
    <tr><td>Iraq</td><td>Arabic</td><td>ar-IQ</td><td>ar-IRQ</td><td>2049</td></tr>
    <tr><td>Iraq</td><td>Kurdish, Sorani</td><td>ckb-IQ</td><td>ckb-IRQ</td><td>4096</td></tr>
    <tr><td>Iraq</td><td>Northern Luri</td><td>lrc-IQ</td><td>lrc-IRQ</td><td>4096</td></tr>
    <tr><td>Iraq</td><td>Syriac</td><td>syr-IQ</td><td>syr-IRQ</td><td>4096</td></tr>
    <tr><td>Ireland</td><td>English</td><td>en-IE</td><td>en-IRL</td><td>6153</td></tr>
    <tr><td>Ireland</td><td>Irish</td><td>ga-IE</td><td>ga-IRL</td><td>2108</td></tr>
    <tr><td>Isle of Man</td><td>English</td><td>en-IM</td><td>en-IMN</td><td>4096</td></tr>
    <tr><td>Isle of Man</td><td>Manx</td><td>gv-IM</td><td>gv-IMN</td><td>4096</td></tr>
    <tr><td>Israel</td><td>Arabic</td><td>ar-IL</td><td>ar-ISR</td><td>4096</td></tr>
    <tr><td>Israel</td><td>English</td><td>en-IL</td><td>en-ISR</td><td>4096</td></tr>
    <tr><td>Israel</td><td>Hebrew</td><td>he-IL</td><td>he-ISR</td><td>1037</td></tr>
    <tr><td>Italy</td><td>Catalan</td><td>ca-IT</td><td>ca-ITA</td><td>4096</td></tr>
    <tr><td>Italy</td><td>English</td><td>en-IT</td><td>en-ITA</td><td>4096</td></tr>
    <tr><td>Italy</td><td>Friulian</td><td>fur-IT</td><td>fur-ITA</td><td>4096</td></tr>
    <tr><td>Italy</td><td>German</td><td>de-IT</td><td>de-ITA</td><td>4096</td></tr>
    <tr><td>Italy</td><td>Italian</td><td>it-IT</td><td>it-ITA</td><td>1040</td></tr>
    <tr><td>Italy</td><td>Sardinian</td><td>sc-IT</td><td>sc-ITA</td><td>4096</td></tr>
    <tr><td>Italy</td><td>Sicilian</td><td>scn-IT</td><td>scn-ITA</td><td>4096</td></tr>
    <tr><td>Jamaica</td><td>English</td><td>en-JM</td><td>en-JAM</td><td>8201</td></tr>
    <tr><td>Japan</td><td>English</td><td>en-JP</td><td>en-JPN</td><td>4096</td></tr>
    <tr><td>Japan</td><td>Japanese</td><td>ja-JP</td><td>ja-JPN</td><td>1041</td></tr>
    <tr><td>Jersey</td><td>English</td><td>en-JE</td><td>en-JEY</td><td>4096</td></tr>
    <tr><td>Jordan</td><td>Arabic</td><td>ar-JO</td><td>ar-JOR</td><td>11265</td></tr>
    <tr><td>Kazakhstan</td><td>Kazakh</td><td>kk-KZ</td><td>kk-KAZ</td><td>1087</td></tr>
    <tr><td>Kazakhstan</td><td>Russian</td><td>ru-KZ</td><td>ru-KAZ</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Embu</td><td>ebu-KE</td><td>ebu-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>English</td><td>en-KE</td><td>en-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Gusii</td><td>guz-KE</td><td>guz-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Kalenjin</td><td>kln-KE</td><td>kln-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Kamba</td><td>kam-KE</td><td>kam-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Kikuyu</td><td>ki-KE</td><td>ki-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Luo</td><td>luo-KE</td><td>luo-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Luyia</td><td>luy-KE</td><td>luy-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Masai</td><td>mas-KE</td><td>mas-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Meru</td><td>mer-KE</td><td>mer-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Oromo</td><td>om-KE</td><td>om-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Samburu</td><td>saq-KE</td><td>saq-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Somali</td><td>so-KE</td><td>so-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Swahili</td><td>sw-KE</td><td>sw-KEN</td><td>1089</td></tr>
    <tr><td>Kenya</td><td>Taita</td><td>dav-KE</td><td>dav-KEN</td><td>4096</td></tr>
    <tr><td>Kenya</td><td>Teso</td><td>teo-KE</td><td>teo-KEN</td><td>4096</td></tr>
    <tr><td>Kiribati</td><td>English</td><td>en-KI</td><td>en-KIR</td><td>4096</td></tr>
    <tr><td>Kosovo</td><td>Albanian</td><td>sq-XK</td><td>sq-XKK</td><td>4096</td></tr>
    <tr><td>Kosovo</td><td>Serbian</td><td>sr-XK</td><td>sr-XKK</td><td>4096</td></tr>
    <tr><td>Kosovo</td><td>Serbian</td><td>sr-XK</td><td>sr-XKK</td><td>4096</td></tr>
    <tr><td>Kuwait</td><td>Arabic</td><td>ar-KW</td><td>ar-KWT</td><td>13313</td></tr>
    <tr><td>Kyrgyzstan</td><td>Kyrgyz</td><td>ky-KG</td><td>ky-KGZ</td><td>1088</td></tr>
    <tr><td>Kyrgyzstan</td><td>Russian</td><td>ru-KG</td><td>ru-KGZ</td><td>4096</td></tr>
    <tr><td>Laos</td><td>Lao</td><td>lo-LA</td><td>lo-LAO</td><td>1108</td></tr>
    <tr><td>Latin America</td><td>Spanish</td><td>es-419</td><td>es-</td><td>22538</td></tr>
    <tr><td>Latvia</td><td>English</td><td>en-LV</td><td>en-LVA</td><td>4096</td></tr>
    <tr><td>Latvia</td><td>Latvian</td><td>lv-LV</td><td>lv-LVA</td><td>1062</td></tr>
    <tr><td>Lebanon</td><td>Arabic</td><td>ar-LB</td><td>ar-LBN</td><td>12289</td></tr>
    <tr><td>Lesotho</td><td>English</td><td>en-LS</td><td>en-LSO</td><td>4096</td></tr>
    <tr><td>Lesotho</td><td>Southern Sotho</td><td>st-LS</td><td>st-LSO</td><td>4096</td></tr>
    <tr><td>Liberia</td><td>English</td><td>en-LR</td><td>en-LBR</td><td>4096</td></tr>
    <tr><td>Liberia</td><td>Fulah</td><td>ff-LR</td><td>ff-LBR</td><td>4096</td></tr>
    <tr><td>Liberia</td><td>Kpelle</td><td>kpe-LR</td><td>kpe-LBR</td><td>4096</td></tr>
    <tr><td>Liberia</td><td>Vai</td><td>vai-LR</td><td>vai-LBR</td><td>4096</td></tr>
    <tr><td>Liberia</td><td>Vai</td><td>vai-LR</td><td>vai-LBR</td><td>4096</td></tr>
    <tr><td>Libya</td><td>Arabic</td><td>ar-LY</td><td>ar-LBY</td><td>4097</td></tr>
    <tr><td>Liechtenstein</td><td>German</td><td>de-LI</td><td>de-LIE</td><td>5127</td></tr>
    <tr><td>Liechtenstein</td><td>Swiss German</td><td>gsw-LI</td><td>gsw-LIE</td><td>4096</td></tr>
    <tr><td>Lithuania</td><td>English</td><td>en-LT</td><td>en-LTU</td><td>4096</td></tr>
    <tr><td>Lithuania</td><td>Lithuanian</td><td>lt-LT</td><td>lt-LTU</td><td>1063</td></tr>
    <tr><td>Luxembourg</td><td>English</td><td>en-LU</td><td>en-LUX</td><td>4096</td></tr>
    <tr><td>Luxembourg</td><td>French</td><td>fr-LU</td><td>fr-LUX</td><td>5132</td></tr>
    <tr><td>Luxembourg</td><td>German</td><td>de-LU</td><td>de-LUX</td><td>4103</td></tr>
    <tr><td>Luxembourg</td><td>Luxembourgish</td><td>lb-LU</td><td>lb-LUX</td><td>1134</td></tr>
    <tr><td>Luxembourg</td><td>Portuguese</td><td>pt-LU</td><td>pt-LUX</td><td>4096</td></tr>
    <tr><td>Macao</td><td>Chinese</td><td>zh-MO</td><td>zh-MAC</td><td>4096</td></tr>
    <tr><td>Macao</td><td>Chinese</td><td>zh-MO</td><td>zh-MAC</td><td>4096</td></tr>
    <tr><td>Macao</td><td>English</td><td>en-MO</td><td>en-MAC</td><td>4096</td></tr>
    <tr><td>Macao</td><td>Portuguese</td><td>pt-MO</td><td>pt-MAC</td><td>4096</td></tr>
    <tr><td>Madagascar</td><td>English</td><td>en-MG</td><td>en-MDG</td><td>4096</td></tr>
    <tr><td>Madagascar</td><td>French</td><td>fr-MG</td><td>fr-MDG</td><td>4096</td></tr>
    <tr><td>Madagascar</td><td>Malagasy</td><td>mg-MG</td><td>mg-MDG</td><td>4096</td></tr>
    <tr><td>Malawi</td><td>English</td><td>en-MW</td><td>en-MWI</td><td>4096</td></tr>
    <tr><td>Malawi</td><td>Nyanja</td><td>ny-MW</td><td>ny-MWI</td><td>4096</td></tr>
    <tr><td>Malaysia</td><td>English</td><td>en-MY</td><td>en-MYS</td><td>17417</td></tr>
    <tr><td>Malaysia</td><td>Malay</td><td>ms-MY</td><td>ms-MYS</td><td>1086</td></tr>
    <tr><td>Malaysia</td><td>Malay</td><td>ms-MY</td><td>ms-MYS</td><td>4096</td></tr>
    <tr><td>Malaysia</td><td>Tamil</td><td>ta-MY</td><td>ta-MYS</td><td>4096</td></tr>
    <tr><td>Maldives</td><td>Dhivehi</td><td>dv-MV</td><td>dv-MDV</td><td>1125</td></tr>
    <tr><td>Maldives</td><td>English</td><td>en-MV</td><td>en-MDV</td><td>4096</td></tr>
    <tr><td>Mali</td><td>Bambara</td><td>bm-ML</td><td>bm-MLI</td><td>4096</td></tr>
    <tr><td>Mali</td><td>French</td><td>fr-ML</td><td>fr-MLI</td><td>13324</td></tr>
    <tr><td>Mali</td><td>Koyra Chiini</td><td>khq-ML</td><td>khq-MLI</td><td>4096</td></tr>
    <tr><td>Mali</td><td>Koyraboro Senni</td><td>ses-ML</td><td>ses-MLI</td><td>4096</td></tr>
    <tr><td>Malta</td><td>English</td><td>en-MT</td><td>en-MLT</td><td>4096</td></tr>
    <tr><td>Malta</td><td>Maltese</td><td>mt-MT</td><td>mt-MLT</td><td>1082</td></tr>
    <tr><td>Marshall Islands</td><td>English</td><td>en-MH</td><td>en-MHL</td><td>4096</td></tr>
    <tr><td>Martinique</td><td>French</td><td>fr-MQ</td><td>fr-MTQ</td><td>4096</td></tr>
    <tr><td>Martinique</td><td>Spanish</td><td>es-MQ</td><td>es-MTQ</td><td>4096</td></tr>
    <tr><td>Mauritania</td><td>Arabic</td><td>ar-MR</td><td>ar-MRT</td><td>4096</td></tr>
    <tr><td>Mauritania</td><td>French</td><td>fr-MR</td><td>fr-MRT</td><td>4096</td></tr>
    <tr><td>Mauritania</td><td>Fulah</td><td>ff-MR</td><td>ff-MRT</td><td>4096</td></tr>
    <tr><td>Mauritius</td><td>English</td><td>en-MU</td><td>en-MUS</td><td>4096</td></tr>
    <tr><td>Mauritius</td><td>French</td><td>fr-MU</td><td>fr-MUS</td><td>4096</td></tr>
    <tr><td>Mauritius</td><td>Morisyen</td><td>mfe-MU</td><td>mfe-MUS</td><td>4096</td></tr>
    <tr><td>Mayotte</td><td>French</td><td>fr-YT</td><td>fr-MYT</td><td>4096</td></tr>
    <tr><td>Mexico</td><td>English</td><td>en-MX</td><td>en-MEX</td><td>4096</td></tr>
    <tr><td>Mexico</td><td>Spanish</td><td>es-MX</td><td>es-MEX</td><td>2058</td></tr>
    <tr><td>Micronesia</td><td>English</td><td>en-FM</td><td>en-FSM</td><td>4096</td></tr>
    <tr><td>Moldova</td><td>Romanian</td><td>ro-MD</td><td>ro-MDA</td><td>2072</td></tr>
    <tr><td>Moldova</td><td>Russian</td><td>ru-MD</td><td>ru-MDA</td><td>2073</td></tr>
    <tr><td>Monaco</td><td>French</td><td>fr-MC</td><td>fr-MCO</td><td>6156</td></tr>
    <tr><td>Mongolia</td><td>Mongolian</td><td>mn-MN</td><td>mn-MNG</td><td>1104</td></tr>
    <tr><td>Montenegro</td><td>English</td><td>en-ME</td><td>en-MNE</td><td>4096</td></tr>
    <tr><td>Montenegro</td><td>Serbian</td><td>sr-ME</td><td>sr-MNE</td><td>11290</td></tr>
    <tr><td>Montenegro</td><td>Serbian</td><td>sr-ME</td><td>sr-MNE</td><td>12314</td></tr>
    <tr><td>Montserrat</td><td>English</td><td>en-MS</td><td>en-MSR</td><td>4096</td></tr>
    <tr><td>Montserrat</td><td>Spanish</td><td>es-MS</td><td>es-MSR</td><td>4096</td></tr>
    <tr><td>Morocco</td><td>Arabic</td><td>ar-MA</td><td>ar-MAR</td><td>6145</td></tr>
    <tr><td>Morocco</td><td>Central Atlas Tamazight</td><td>tzm-MA</td><td>tzm-MAR</td><td>4096</td></tr>
    <tr><td>Morocco</td><td>French</td><td>fr-MA</td><td>fr-MAR</td><td>14348</td></tr>
    <tr><td>Morocco</td><td>Standard Moroccan Tamazight</td><td>zgh-MA</td><td>zgh-MAR</td><td>4096</td></tr>
    <tr><td>Morocco</td><td>Tachelhit</td><td>shi-MA</td><td>shi-MAR</td><td>4096</td></tr>
    <tr><td>Morocco</td><td>Tachelhit</td><td>shi-MA</td><td>shi-MAR</td><td>4096</td></tr>
    <tr><td>Mozambique</td><td>Makhuwa-Meetto</td><td>mgh-MZ</td><td>mgh-MOZ</td><td>4096</td></tr>
    <tr><td>Mozambique</td><td>Portuguese</td><td>pt-MZ</td><td>pt-MOZ</td><td>4096</td></tr>
    <tr><td>Mozambique</td><td>Sena</td><td>seh-MZ</td><td>seh-MOZ</td><td>4096</td></tr>
    <tr><td>Myanmar (Burma)</td><td>Burmese</td><td>my-MM</td><td>my-MMR</td><td>1109</td></tr>
    <tr><td>Myanmar (Burma)</td><td>English</td><td>en-MM</td><td>en-MMR</td><td>4096</td></tr>
    <tr><td>Namibia</td><td>Afrikaans</td><td>af-NA</td><td>af-NAM</td><td>4096</td></tr>
    <tr><td>Namibia</td><td>English</td><td>en-NA</td><td>en-NAM</td><td>4096</td></tr>
    <tr><td>Namibia</td><td>Nama</td><td>naq-NA</td><td>naq-NAM</td><td>4096</td></tr>
    <tr><td>Nauru</td><td>English</td><td>en-NR</td><td>en-NRU</td><td>4096</td></tr>
    <tr><td>Nepal</td><td>Nepali</td><td>ne-NP</td><td>ne-NPL</td><td>1121</td></tr>
    <tr><td>Netherlands</td><td>Dutch</td><td>nl-NL</td><td>nl-NLD</td><td>1043</td></tr>
    <tr><td>Netherlands</td><td>English</td><td>en-NL</td><td>en-NLD</td><td>4096</td></tr>
    <tr><td>Netherlands</td><td>Low German</td><td>nds-NL</td><td>nds-NLD</td><td>4096</td></tr>
    <tr><td>Netherlands</td><td>Western Frisian</td><td>fy-NL</td><td>fy-NLD</td><td>1122</td></tr>
    <tr><td>New Caledonia</td><td>French</td><td>fr-NC</td><td>fr-NCL</td><td>4096</td></tr>
    <tr><td>New Zealand</td><td>English</td><td>en-NZ</td><td>en-NZL</td><td>5129</td></tr>
    <tr><td>New Zealand</td><td>Maori</td><td>mi-NZ</td><td>mi-NZL</td><td>1153</td></tr>
    <tr><td>Nicaragua</td><td>Spanish</td><td>es-NI</td><td>es-NIC</td><td>19466</td></tr>
    <tr><td>Niger</td><td>French</td><td>fr-NE</td><td>fr-NER</td><td>4096</td></tr>
    <tr><td>Niger</td><td>Fulah</td><td>ff-NE</td><td>ff-NER</td><td>4096</td></tr>
    <tr><td>Niger</td><td>Hausa</td><td>ha-NE</td><td>ha-NER</td><td>4096</td></tr>
    <tr><td>Niger</td><td>Tasawaq</td><td>twq-NE</td><td>twq-NER</td><td>4096</td></tr>
    <tr><td>Niger</td><td>Zarma</td><td>dje-NE</td><td>dje-NER</td><td>4096</td></tr>
    <tr><td>Nigeria</td><td>English</td><td>en-NG</td><td>en-NGA</td><td>4096</td></tr>
    <tr><td>Nigeria</td><td>Fulah</td><td>ff-NG</td><td>ff-NGA</td><td>4096</td></tr>
    <tr><td>Nigeria</td><td>Hausa</td><td>ha-NG</td><td>ha-NGA</td><td>4096</td></tr>
    <tr><td>Nigeria</td><td>Igbo</td><td>ig-NG</td><td>ig-NGA</td><td>1136</td></tr>
    <tr><td>Nigeria</td><td>Jju</td><td>kaj-NG</td><td>kaj-NGA</td><td>4096</td></tr>
    <tr><td>Nigeria</td><td>Tyap</td><td>kcg-NG</td><td>kcg-NGA</td><td>4096</td></tr>
    <tr><td>Nigeria</td><td>Yoruba</td><td>yo-NG</td><td>yo-NGA</td><td>1130</td></tr>
    <tr><td>Niue</td><td>English</td><td>en-NU</td><td>en-NIU</td><td>4096</td></tr>
    <tr><td>Norfolk Island</td><td>English</td><td>en-NF</td><td>en-NFK</td><td>4096</td></tr>
    <tr><td>North Korea</td><td>Korean</td><td>ko-KP</td><td>ko-PRK</td><td>4096</td></tr>
    <tr><td>North Macedonia</td><td>Albanian</td><td>sq-MK</td><td>sq-MKD</td><td>4096</td></tr>
    <tr><td>North Macedonia</td><td>Macedonian</td><td>mk-MK</td><td>mk-MKD</td><td>1071</td></tr>
    <tr><td>Northern Mariana Islands</td><td>English</td><td>en-MP</td><td>en-MNP</td><td>4096</td></tr>
    <tr><td>Norway</td><td>English</td><td>en-NO</td><td>en-NOR</td><td>4096</td></tr>
    <tr><td>Norway</td><td>Northern Sami</td><td>se-NO</td><td>se-NOR</td><td>1083</td></tr>
    <tr><td>Norway</td><td>Norwegian Bokmål</td><td>nb-NO</td><td>nb-NOR</td><td>1044</td></tr>
    <tr><td>Norway</td><td>Norwegian Nynorsk</td><td>nn-NO</td><td>nn-NOR</td><td>2068</td></tr>
    <tr><td>Oman</td><td>Arabic</td><td>ar-OM</td><td>ar-OMN</td><td>8193</td></tr>
    <tr><td>Pakistan</td><td>English</td><td>en-PK</td><td>en-PAK</td><td>4096</td></tr>
    <tr><td>Pakistan</td><td>Pashto</td><td>ps-PK</td><td>ps-PAK</td><td>4096</td></tr>
    <tr><td>Pakistan</td><td>Punjabi</td><td>pa-PK</td><td>pa-PAK</td><td>2118</td></tr>
    <tr><td>Pakistan</td><td>Punjabi</td><td>pa-PK</td><td>pa-PAK</td><td>4096</td></tr>
    <tr><td>Pakistan</td><td>Sindhi</td><td>sd-PK</td><td>sd-PAK</td><td>4096</td></tr>
    <tr><td>Pakistan</td><td>Urdu</td><td>ur-PK</td><td>ur-PAK</td><td>1056</td></tr>
    <tr><td>Pakistan</td><td>Urdu</td><td>ur-PK</td><td>ur-PAK</td><td>4096</td></tr>
    <tr><td>Pakistan</td><td>Urdu</td><td>ur-PK</td><td>ur-PAK</td><td>4096</td></tr>
    <tr><td>Palau</td><td>English</td><td>en-PW</td><td>en-PLW</td><td>4096</td></tr>
    <tr><td>Palestinian Territories</td><td>Arabic</td><td>ar-PS</td><td>ar-PSE</td><td>4096</td></tr>
    <tr><td>Panama</td><td>Spanish</td><td>es-PA</td><td>es-PAN</td><td>6154</td></tr>
    <tr><td>Papua New Guinea</td><td>English</td><td>en-PG</td><td>en-PNG</td><td>4096</td></tr>
    <tr><td>Paraguay</td><td>Guarani</td><td>gn-PY</td><td>gn-PRY</td><td>1140</td></tr>
    <tr><td>Paraguay</td><td>Spanish</td><td>es-PY</td><td>es-PRY</td><td>15370</td></tr>
    <tr><td>Peru</td><td>Quechua</td><td>qu-PE</td><td>qu-PER</td><td>4096</td></tr>
    <tr><td>Peru</td><td>Spanish</td><td>es-PE</td><td>es-PER</td><td>10250</td></tr>
    <tr><td>Philippines</td><td>Cebuano</td><td>ceb-PH</td><td>ceb-PHL</td><td>4096</td></tr>
    <tr><td>Philippines</td><td>English</td><td>en-PH</td><td>en-PHL</td><td>13321</td></tr>
    <tr><td>Philippines</td><td>Filipino</td><td>fil-PH</td><td>fil-PHL</td><td>1124</td></tr>
    <tr><td>Philippines</td><td>Spanish</td><td>es-PH</td><td>es-PHL</td><td>4096</td></tr>
    <tr><td>Pitcairn Islands</td><td>English</td><td>en-PN</td><td>en-PCN</td><td>4096</td></tr>
    <tr><td>Poland</td><td>English</td><td>en-PL</td><td>en-POL</td><td>4096</td></tr>
    <tr><td>Poland</td><td>Polish</td><td>pl-PL</td><td>pl-POL</td><td>1045</td></tr>
    <tr><td>Portugal</td><td>English</td><td>en-PT</td><td>en-PRT</td><td>4096</td></tr>
    <tr><td>Portugal</td><td>Portuguese</td><td>pt-PT</td><td>pt-PRT</td><td>2070</td></tr>
    <tr><td>Puerto Rico</td><td>English</td><td>en-PR</td><td>en-PRI</td><td>4096</td></tr>
    <tr><td>Puerto Rico</td><td>Spanish</td><td>es-PR</td><td>es-PRI</td><td>20490</td></tr>
    <tr><td>Qatar</td><td>Arabic</td><td>ar-QA</td><td>ar-QAT</td><td>16385</td></tr>
    <tr><td>Réunion</td><td>French</td><td>fr-RE</td><td>fr-REU</td><td>8204</td></tr>
    <tr><td>Romania</td><td>English</td><td>en-RO</td><td>en-ROU</td><td>4096</td></tr>
    <tr><td>Romania</td><td>Romanian</td><td>ro-RO</td><td>ro-ROU</td><td>1048</td></tr>
    <tr><td>Russia</td><td>Bashkir</td><td>ba-RU</td><td>ba-RUS</td><td>1133</td></tr>
    <tr><td>Russia</td><td>Chechen</td><td>ce-RU</td><td>ce-RUS</td><td>4096</td></tr>
    <tr><td>Russia</td><td>Chuvash</td><td>cv-RU</td><td>cv-RUS</td><td>4096</td></tr>
    <tr><td>Russia</td><td>English</td><td>en-RU</td><td>en-RUS</td><td>4096</td></tr>
    <tr><td>Russia</td><td>Erzya</td><td>myv-RU</td><td>myv-RUS</td><td>4096</td></tr>
    <tr><td>Russia</td><td>Ossetic</td><td>os-RU</td><td>os-RUS</td><td>4096</td></tr>
    <tr><td>Russia</td><td>Russian</td><td>ru-RU</td><td>ru-RUS</td><td>1049</td></tr>
    <tr><td>Russia</td><td>Sakha</td><td>sah-RU</td><td>sah-RUS</td><td>1157</td></tr>
    <tr><td>Russia</td><td>Tatar</td><td>tt-RU</td><td>tt-RUS</td><td>1092</td></tr>
    <tr><td>Rwanda</td><td>English</td><td>en-RW</td><td>en-RWA</td><td>4096</td></tr>
    <tr><td>Rwanda</td><td>French</td><td>fr-RW</td><td>fr-RWA</td><td>4096</td></tr>
    <tr><td>Rwanda</td><td>Kinyarwanda</td><td>rw-RW</td><td>rw-RWA</td><td>1159</td></tr>
    <tr><td>Samoa</td><td>English</td><td>en-WS</td><td>en-WSM</td><td>4096</td></tr>
    <tr><td>San Marino</td><td>Italian</td><td>it-SM</td><td>it-SMR</td><td>4096</td></tr>
    <tr><td>São Tomé &amp; Príncipe</td><td>Portuguese</td><td>pt-ST</td><td>pt-STP</td><td>4096</td></tr>
    <tr><td>Saudi Arabia</td><td>Arabic</td><td>ar-SA</td><td>ar-SAU</td><td>1025</td></tr>
    <tr><td>Saudi Arabia</td><td>English</td><td>en-SA</td><td>en-SAU</td><td>4096</td></tr>
    <tr><td>Senegal</td><td>French</td><td>fr-SN</td><td>fr-SEN</td><td>10252</td></tr>
    <tr><td>Senegal</td><td>Fulah</td><td>ff-SN</td><td>ff-SEN</td><td>2151</td></tr>
    <tr><td>Senegal</td><td>Jola-Fonyi</td><td>dyo-SN</td><td>dyo-SEN</td><td>4096</td></tr>
    <tr><td>Senegal</td><td>Wolof</td><td>wo-SN</td><td>wo-SEN</td><td>1160</td></tr>
    <tr><td>Serbia</td><td>English</td><td>en-RS</td><td>en-SRB</td><td>4096</td></tr>
    <tr><td>Serbia</td><td>Serbian</td><td>sr-RS</td><td>sr-SRB</td><td>10266</td></tr>
    <tr><td>Serbia</td><td>Serbian</td><td>sr-RS</td><td>sr-SRB</td><td>9242</td></tr>
    <tr><td>Seychelles</td><td>English</td><td>en-SC</td><td>en-SYC</td><td>4096</td></tr>
    <tr><td>Seychelles</td><td>French</td><td>fr-SC</td><td>fr-SYC</td><td>4096</td></tr>
    <tr><td>Sierra Leone</td><td>English</td><td>en-SL</td><td>en-SLE</td><td>4096</td></tr>
    <tr><td>Sierra Leone</td><td>Fulah</td><td>ff-SL</td><td>ff-SLE</td><td>4096</td></tr>
    <tr><td>Singapore</td><td>Chinese</td><td>zh-SG</td><td>zh-SGP</td><td>4096</td></tr>
    <tr><td>Singapore</td><td>English</td><td>en-SG</td><td>en-SGP</td><td>18441</td></tr>
    <tr><td>Singapore</td><td>Malay</td><td>ms-SG</td><td>ms-SGP</td><td>4096</td></tr>
    <tr><td>Singapore</td><td>Tamil</td><td>ta-SG</td><td>ta-SGP</td><td>4096</td></tr>
    <tr><td>Sint Maarten</td><td>Dutch</td><td>nl-SX</td><td>nl-SXM</td><td>4096</td></tr>
    <tr><td>Sint Maarten</td><td>English</td><td>en-SX</td><td>en-SXM</td><td>4096</td></tr>
    <tr><td>Sint Maarten</td><td>Spanish</td><td>es-SX</td><td>es-SXM</td><td>4096</td></tr>
    <tr><td>Slovakia</td><td>English</td><td>en-SK</td><td>en-SVK</td><td>4096</td></tr>
    <tr><td>Slovakia</td><td>Slovak</td><td>sk-SK</td><td>sk-SVK</td><td>1051</td></tr>
    <tr><td>Slovenia</td><td>English</td><td>en-SI</td><td>en-SVN</td><td>4096</td></tr>
    <tr><td>Slovenia</td><td>Slovenian</td><td>sl-SI</td><td>sl-SVN</td><td>1060</td></tr>
    <tr><td>Solomon Islands</td><td>English</td><td>en-SB</td><td>en-SLB</td><td>4096</td></tr>
    <tr><td>Somalia</td><td>Arabic</td><td>ar-SO</td><td>ar-SOM</td><td>4096</td></tr>
    <tr><td>Somalia</td><td>Somali</td><td>so-SO</td><td>so-SOM</td><td>1143</td></tr>
    <tr><td>South Africa</td><td>Afrikaans</td><td>af-ZA</td><td>af-ZAF</td><td>1078</td></tr>
    <tr><td>South Africa</td><td>English</td><td>en-ZA</td><td>en-ZAF</td><td>7177</td></tr>
    <tr><td>South Africa</td><td>Northern Sotho</td><td>nso-ZA</td><td>nso-ZAF</td><td>1132</td></tr>
    <tr><td>South Africa</td><td>South Ndebele</td><td>nr-ZA</td><td>nr-ZAF</td><td>4096</td></tr>
    <tr><td>South Africa</td><td>Southern Sotho</td><td>st-ZA</td><td>st-ZAF</td><td>1072</td></tr>
    <tr><td>South Africa</td><td>Swati</td><td>ss-ZA</td><td>ss-ZAF</td><td>4096</td></tr>
    <tr><td>South Africa</td><td>Tsonga</td><td>ts-ZA</td><td>ts-ZAF</td><td>1073</td></tr>
    <tr><td>South Africa</td><td>Tswana</td><td>tn-ZA</td><td>tn-ZAF</td><td>1074</td></tr>
    <tr><td>South Africa</td><td>Venda</td><td>ve-ZA</td><td>ve-ZAF</td><td>1075</td></tr>
    <tr><td>South Africa</td><td>Xhosa</td><td>xh-ZA</td><td>xh-ZAF</td><td>1076</td></tr>
    <tr><td>South Africa</td><td>Zulu</td><td>zu-ZA</td><td>zu-ZAF</td><td>1077</td></tr>
    <tr><td>South Korea</td><td>English</td><td>en-KR</td><td>en-KOR</td><td>4096</td></tr>
    <tr><td>South Korea</td><td>Korean</td><td>ko-KR</td><td>ko-KOR</td><td>1042</td></tr>
    <tr><td>South Sudan</td><td>Arabic</td><td>ar-SS</td><td>ar-SSD</td><td>4096</td></tr>
    <tr><td>South Sudan</td><td>English</td><td>en-SS</td><td>en-SSD</td><td>4096</td></tr>
    <tr><td>South Sudan</td><td>Nuer</td><td>nus-SS</td><td>nus-SSD</td><td>4096</td></tr>
    <tr><td>Spain</td><td>Asturian</td><td>ast-ES</td><td>ast-ESP</td><td>4096</td></tr>
    <tr><td>Spain</td><td>Basque</td><td>eu-ES</td><td>eu-ESP</td><td>1069</td></tr>
    <tr><td>Spain</td><td>Catalan</td><td>ca-ES</td><td>ca-ESP</td><td>1027</td></tr>
    <tr><td>Spain</td><td>English</td><td>en-ES</td><td>en-ESP</td><td>4096</td></tr>
    <tr><td>Spain</td><td>Galician</td><td>gl-ES</td><td>gl-ESP</td><td>1110</td></tr>
    <tr><td>Spain</td><td>Spanish</td><td>es-ES</td><td>es-ESP</td><td>3082</td></tr>
    <tr><td>Sri Lanka</td><td>Sinhala</td><td>si-LK</td><td>si-LKA</td><td>1115</td></tr>
    <tr><td>Sri Lanka</td><td>Tamil</td><td>ta-LK</td><td>ta-LKA</td><td>2121</td></tr>
    <tr><td>St. Barthélemy</td><td>French</td><td>fr-BL</td><td>fr-BLM</td><td>4096</td></tr>
    <tr><td>St. Barthélemy</td><td>Spanish</td><td>es-BL</td><td>es-BLM</td><td>4096</td></tr>
    <tr><td>St. Helena</td><td>English</td><td>en-SH</td><td>en-SHN</td><td>4096</td></tr>
    <tr><td>St. Kitts &amp; Nevis</td><td>English</td><td>en-KN</td><td>en-KNA</td><td>4096</td></tr>
    <tr><td>St. Kitts &amp; Nevis</td><td>Spanish</td><td>es-KN</td><td>es-KNA</td><td>4096</td></tr>
    <tr><td>St. Lucia</td><td>English</td><td>en-LC</td><td>en-LCA</td><td>4096</td></tr>
    <tr><td>St. Lucia</td><td>Spanish</td><td>es-LC</td><td>es-LCA</td><td>4096</td></tr>
    <tr><td>St. Martin</td><td>French</td><td>fr-MF</td><td>fr-MAF</td><td>4096</td></tr>
    <tr><td>St. Martin</td><td>Spanish</td><td>es-MF</td><td>es-MAF</td><td>4096</td></tr>
    <tr><td>St. Pierre &amp; Miquelon</td><td>French</td><td>fr-PM</td><td>fr-SPM</td><td>4096</td></tr>
    <tr><td>St. Pierre &amp; Miquelon</td><td>Spanish</td><td>es-PM</td><td>es-SPM</td><td>4096</td></tr>
    <tr><td>St. Vincent &amp; Grenadines</td><td>English</td><td>en-VC</td><td>en-VCT</td><td>4096</td></tr>
    <tr><td>St. Vincent &amp; Grenadines</td><td>Spanish</td><td>es-VC</td><td>es-VCT</td><td>4096</td></tr>
    <tr><td>Sudan</td><td>Arabic</td><td>ar-SD</td><td>ar-SDN</td><td>4096</td></tr>
    <tr><td>Sudan</td><td>English</td><td>en-SD</td><td>en-SDN</td><td>4096</td></tr>
    <tr><td>Suriname</td><td>Dutch</td><td>nl-SR</td><td>nl-SUR</td><td>4096</td></tr>
    <tr><td>Suriname</td><td>Spanish</td><td>es-SR</td><td>es-SUR</td><td>4096</td></tr>
    <tr><td>Svalbard &amp; Jan Mayen</td><td>Norwegian Bokmål</td><td>nb-SJ</td><td>nb-SJM</td><td>4096</td></tr>
    <tr><td>Sweden</td><td>English</td><td>en-SE</td><td>en-SWE</td><td>4096</td></tr>
    <tr><td>Sweden</td><td>Northern Sami</td><td>se-SE</td><td>se-SWE</td><td>2107</td></tr>
    <tr><td>Sweden</td><td>Swedish</td><td>sv-SE</td><td>sv-SWE</td><td>1053</td></tr>
    <tr><td>Switzerland</td><td>English</td><td>en-CH</td><td>en-CHE</td><td>4096</td></tr>
    <tr><td>Switzerland</td><td>French</td><td>fr-CH</td><td>fr-CHE</td><td>4108</td></tr>
    <tr><td>Switzerland</td><td>German</td><td>de-CH</td><td>de-CHE</td><td>2055</td></tr>
    <tr><td>Switzerland</td><td>Italian</td><td>it-CH</td><td>it-CHE</td><td>2064</td></tr>
    <tr><td>Switzerland</td><td>Portuguese</td><td>pt-CH</td><td>pt-CHE</td><td>4096</td></tr>
    <tr><td>Switzerland</td><td>Romansh</td><td>rm-CH</td><td>rm-CHE</td><td>1047</td></tr>
    <tr><td>Switzerland</td><td>Swiss German</td><td>gsw-CH</td><td>gsw-CHE</td><td>4096</td></tr>
    <tr><td>Switzerland</td><td>Walser</td><td>wae-CH</td><td>wae-CHE</td><td>4096</td></tr>
    <tr><td>Syria</td><td>Arabic</td><td>ar-SY</td><td>ar-SYR</td><td>10241</td></tr>
    <tr><td>Syria</td><td>French</td><td>fr-SY</td><td>fr-SYR</td><td>4096</td></tr>
    <tr><td>Syria</td><td>Syriac</td><td>syr-SY</td><td>syr-SYR</td><td>1114</td></tr>
    <tr><td>Taiwan</td><td>Chinese</td><td>zh-TW</td><td>zh-TWN</td><td>4096</td></tr>
    <tr><td>Taiwan</td><td>English</td><td>en-TW</td><td>en-TWN</td><td>4096</td></tr>
    <tr><td>Taiwan</td><td>Taroko</td><td>trv-TW</td><td>trv-TWN</td><td>4096</td></tr>
    <tr><td>Tajikistan</td><td>Tajik</td><td>tg-TJ</td><td>tg-TJK</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Asu</td><td>asa-TZ</td><td>asa-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Bena</td><td>bez-TZ</td><td>bez-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>English</td><td>en-TZ</td><td>en-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Langi</td><td>lag-TZ</td><td>lag-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Machame</td><td>jmc-TZ</td><td>jmc-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Makonde</td><td>kde-TZ</td><td>kde-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Masai</td><td>mas-TZ</td><td>mas-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Rombo</td><td>rof-TZ</td><td>rof-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Rwa</td><td>rwk-TZ</td><td>rwk-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Sangu</td><td>sbp-TZ</td><td>sbp-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Shambala</td><td>ksb-TZ</td><td>ksb-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Swahili</td><td>sw-TZ</td><td>sw-TZA</td><td>4096</td></tr>
    <tr><td>Tanzania</td><td>Vunjo</td><td>vun-TZ</td><td>vun-TZA</td><td>4096</td></tr>
    <tr><td>Thailand</td><td>English</td><td>en-TH</td><td>en-THA</td><td>4096</td></tr>
    <tr><td>Thailand</td><td>Thai</td><td>th-TH</td><td>th-THA</td><td>1054</td></tr>
    <tr><td>Timor-Leste</td><td>Portuguese</td><td>pt-TL</td><td>pt-TLS</td><td>4096</td></tr>
    <tr><td>Togo</td><td>Ewe</td><td>ee-TG</td><td>ee-TGO</td><td>4096</td></tr>
    <tr><td>Togo</td><td>French</td><td>fr-TG</td><td>fr-TGO</td><td>4096</td></tr>
    <tr><td>Tokelau</td><td>English</td><td>en-TK</td><td>en-TKL</td><td>4096</td></tr>
    <tr><td>Tonga</td><td>English</td><td>en-TO</td><td>en-TON</td><td>4096</td></tr>
    <tr><td>Tonga</td><td>Tongan</td><td>to-TO</td><td>to-TON</td><td>4096</td></tr>
    <tr><td>Trinidad &amp; Tobago</td><td>English</td><td>en-TT</td><td>en-TTO</td><td>11273</td></tr>
    <tr><td>Trinidad &amp; Tobago</td><td>Spanish</td><td>es-TT</td><td>es-TTO</td><td>4096</td></tr>
    <tr><td>Tunisia</td><td>Arabic</td><td>ar-TN</td><td>ar-TUN</td><td>7169</td></tr>
    <tr><td>Tunisia</td><td>French</td><td>fr-TN</td><td>fr-TUN</td><td>4096</td></tr>
    <tr><td>Turkey</td><td>English</td><td>en-TR</td><td>en-TUR</td><td>4096</td></tr>
    <tr><td>Turkey</td><td>Kurdish</td><td>ku-TR</td><td>ku-TUR</td><td>4096</td></tr>
    <tr><td>Turkey</td><td>Turkish</td><td>tr-TR</td><td>tr-TUR</td><td>1055</td></tr>
    <tr><td>Turkmenistan</td><td>Turkmen</td><td>tk-TM</td><td>tk-TKM</td><td>1090</td></tr>
    <tr><td>Turks &amp; Caicos Islands</td><td>English</td><td>en-TC</td><td>en-TCA</td><td>4096</td></tr>
    <tr><td>Turks &amp; Caicos Islands</td><td>Spanish</td><td>es-TC</td><td>es-TCA</td><td>4096</td></tr>
    <tr><td>Tuvalu</td><td>English</td><td>en-TV</td><td>en-TUV</td><td>4096</td></tr>
    <tr><td>U.S. Outlying Islands</td><td>English</td><td>en-UM</td><td>en-UMI</td><td>4096</td></tr>
    <tr><td>U.S. Virgin Islands</td><td>English</td><td>en-VI</td><td>en-VIR</td><td>4096</td></tr>
    <tr><td>U.S. Virgin Islands</td><td>Spanish</td><td>es-VI</td><td>es-VIR</td><td>4096</td></tr>
    <tr><td>Uganda</td><td>Chiga</td><td>cgg-UG</td><td>cgg-UGA</td><td>4096</td></tr>
    <tr><td>Uganda</td><td>English</td><td>en-UG</td><td>en-UGA</td><td>4096</td></tr>
    <tr><td>Uganda</td><td>Ganda</td><td>lg-UG</td><td>lg-UGA</td><td>4096</td></tr>
    <tr><td>Uganda</td><td>Nyankole</td><td>nyn-UG</td><td>nyn-UGA</td><td>4096</td></tr>
    <tr><td>Uganda</td><td>Soga</td><td>xog-UG</td><td>xog-UGA</td><td>4096</td></tr>
    <tr><td>Uganda</td><td>Swahili</td><td>sw-UG</td><td>sw-UGA</td><td>4096</td></tr>
    <tr><td>Uganda</td><td>Teso</td><td>teo-UG</td><td>teo-UGA</td><td>4096</td></tr>
    <tr><td>Ukraine</td><td>English</td><td>en-UA</td><td>en-UKR</td><td>4096</td></tr>
    <tr><td>Ukraine</td><td>Russian</td><td>ru-UA</td><td>ru-UKR</td><td>4096</td></tr>
    <tr><td>Ukraine</td><td>Ukrainian</td><td>uk-UA</td><td>uk-UKR</td><td>1058</td></tr>
    <tr><td>United Arab Emirates</td><td>Arabic</td><td>ar-AE</td><td>ar-ARE</td><td>14337</td></tr>
    <tr><td>United Arab Emirates</td><td>English</td><td>en-AE</td><td>en-ARE</td><td>4096</td></tr>
    <tr><td>United Kingdom</td><td>Cornish</td><td>kw-GB</td><td>kw-GBR</td><td>4096</td></tr>
    <tr><td>United Kingdom</td><td>English</td><td>en-GB</td><td>en-GBR</td><td>2057</td></tr>
    <tr><td>United Kingdom</td><td>Scottish Gaelic</td><td>gd-GB</td><td>gd-GBR</td><td>1169</td></tr>
    <tr><td>United Kingdom</td><td>Welsh</td><td>cy-GB</td><td>cy-GBR</td><td>1106</td></tr>
    <tr><td>United States</td><td>Cherokee</td><td>chr-US</td><td>chr-USA</td><td>4096</td></tr>
    <tr><td>United States</td><td>English (United States)</td><td>en-US</td><td>en-USA</td><td>4096</td></tr>
    <tr><td>United States</td><td>English</td><td>en-US</td><td>en-USA</td><td>1033</td></tr>
    <tr><td>United States</td><td>Hawaiian</td><td>haw-US</td><td>haw-USA</td><td>1141</td></tr>
    <tr><td>United States</td><td>Lakota</td><td>lkt-US</td><td>lkt-USA</td><td>4096</td></tr>
    <tr><td>United States</td><td>Spanish</td><td>es-US</td><td>es-USA</td><td>21514</td></tr>
    <tr><td>Uruguay</td><td>Spanish</td><td>es-UY</td><td>es-URY</td><td>14346</td></tr>
    <tr><td>Uzbekistan</td><td>Uzbek</td><td>uz-UZ</td><td>uz-UZB</td><td>1091</td></tr>
    <tr><td>Uzbekistan</td><td>Uzbek</td><td>uz-UZ</td><td>uz-UZB</td><td>2115</td></tr>
    <tr><td>Vanuatu</td><td>English</td><td>en-VU</td><td>en-VUT</td><td>4096</td></tr>
    <tr><td>Vanuatu</td><td>French</td><td>fr-VU</td><td>fr-VUT</td><td>4096</td></tr>
    <tr><td>Vatican City</td><td>Italian</td><td>it-VA</td><td>it-VAT</td><td>4096</td></tr>
    <tr><td>Venezuela</td><td>Spanish</td><td>es-VE</td><td>es-VEN</td><td>8202</td></tr>
    <tr><td>Vietnam</td><td>Vietnamese</td><td>vi-VN</td><td>vi-VNM</td><td>1066</td></tr>
    <tr><td>Wallis &amp; Futuna</td><td>French</td><td>fr-WF</td><td>fr-WLF</td><td>4096</td></tr>
    <tr><td>Western Sahara</td><td>Arabic</td><td>ar-EH</td><td>ar-ESH</td><td>4096</td></tr>
    <tr><td>World</td><td>Arabic</td><td>ar-001</td><td>ar-</td><td>4096</td></tr>
    <tr><td>World</td><td>English</td><td>en-001</td><td>en-</td><td>4096</td></tr>
    <tr><td>World</td><td>Esperanto</td><td>eo-001</td><td>eo-</td><td>4096</td></tr>
    <tr><td>World</td><td>Ido</td><td>io-001</td><td>io-</td><td>4096</td></tr>
    <tr><td>World</td><td>Interlingua</td><td>ia-001</td><td>ia-</td><td>4096</td></tr>
    <tr><td>World</td><td>Lojban</td><td>jbo-001</td><td>jbo-</td><td>4096</td></tr>
    <tr><td>World</td><td>Yiddish</td><td>yi-001</td><td>yi-</td><td>1085</td></tr>
    <tr><td>Yemen</td><td>Arabic</td><td>ar-YE</td><td>ar-YEM</td><td>9217</td></tr>
    <tr><td>Zambia</td><td>Bemba</td><td>bem-ZM</td><td>bem-ZMB</td><td>4096</td></tr>
    <tr><td>Zambia</td><td>English</td><td>en-ZM</td><td>en-ZMB</td><td>4096</td></tr>
    <tr><td>Zimbabwe</td><td>English</td><td>en-ZW</td><td>en-ZWE</td><td>12297</td></tr>
    <tr><td>Zimbabwe</td><td>North Ndebele</td><td>nd-ZW</td><td>nd-ZWE</td><td>4096</td></tr>
    <tr><td>Zimbabwe</td><td>Shona</td><td>sn-ZW</td><td>sn-ZWE</td><td>4096</td></tr>
    </tbody></table>
"""


def get_languages()->list:
    languages = []
    soup = Soup(text, 'html.parser')
    trList = soup.find_all("tr")
    for tr in trList:
        data = [td.text for td in tr ]
        if data[0] != "Country" and data[0] != "World":
            language = Language(country=data[0], language=data[1], iso2=data[2], iso3=data[3], id=data[4])
            languages.append(language)
            print(language)
    return languages


language_list = get_languages()

saveToJson(language_list, "languages.json")