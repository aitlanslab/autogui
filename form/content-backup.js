const COUNTRY_NAME_TO_ID = {
  "Afghanistan": "1",
  "Albania": "2",
  "Algeria": "3",
  "American Samoa": "4",
  "Angola": "5",
  "Anguilla": "6",
  "Antartica": "7",
  "Antigua and Barbuda": "8",
  "Argentina": "9",
  "Armenia": "10",
  "Aruba": "11",
  "Ashmore and Cartier Island": "12",
  "Australia": "13",
  "Austria": "14",
  "Azerbaijan": "15",
  "Bahamas": "16",
  "Bahrain": "17",
  "Bangladesh": "18",
  "Barbados": "19",
  "Belarus": "20",
  "Belgium": "21",
  "Belize": "22",
  "Benin": "23",
  "Bermuda": "24",
  "Bhutan": "25",
  "Bolivia": "26",
  "Bosnia and Herzegovina": "27",
  "Botswana": "28",
  "Brazil": "29",
  "British Virgin Islands": "30",
  "Brunei": "31",
  "Bulgaria": "32",
  "Burkina Faso": "33",
  "Burma": "34",
  "Burundi": "35",
  "Cambodia": "36",
  "Cameroon": "37",
  "Canada": "38",
  "Cape Verde": "39",
  "Cayman Islands": "40",
  "Central African Republic": "41",
  "Chad": "42",
  "Chile": "43",
  "China": "44",
  "Christmas Island": "45",
  "Clipperton Island": "46",
  "Cocos (Keeling) Islands": "47",
  "Colombia": "48",
  "Comoros": "49",
  "Congo, Democratic Republic of the": "50",
  "Congo, Republic of the": "51",
  "Cook Islands": "52",
  "Costa Rica": "53",
  "Cote dIvoire": "54",
  "Croatia": "55",
  "Cuba": "56",
  "Cyprus": "57",
  "Czeck Republic": "58",
  "Denmark": "59",
  "Djibouti": "60",
  "Dominica": "61",
  "Dominican Republic": "62",
  "Ecuador": "63",
  "Egypt": "64",
  "El Salvador": "65",
  "Equatorial Guinea": "66",
  "Eritrea": "67",
  "Estonia": "68",
  "Ethiopia": "69",
  "Europa Island": "70",
  "Falkland Islands (Islas Malvinas)": "71",
  "Faroe Islands": "72",
  "Fiji": "73",
  "Finland": "74",
  "France": "75",
  "French Guiana": "76",
  "French Polynesia": "77",
  "French Southern and Antarctic Lands": "78",
  "Gabon": "79",
  "Gambia, The": "80",
  "Gaza Strip": "81",
  "Georgia": "82",
  "Germany": "83",
  "Ghana": "84",
  "Gibraltar": "85",
  "Glorioso Islands": "86",
  "Greece": "87",
  "Greenland": "88",
  "Grenada": "89",
  "Guadeloupe": "90",
  "Guam": "91",
  "Guatemala": "92",
  "Guernsey": "93",
  "Guinea": "94",
  "Guinea-Bissau": "95",
  "Guyana": "96",
  "Haiti": "97",
  "Heard Island and McDonald Islands": "98",
  "Holy See (Vatican City)": "99",
  "Honduras": "100",
  "Hong Kong": "101",
  "Howland Island": "102",
  "Hungary": "103",
  "Iceland": "104",
  "India": "105",
  "Indonesia": "106",
  "Iran": "107",
  "Iraq": "108",
  "Ireland": "109",
  "Ireland, Northern": "110",
  "Israel": "111",
  "Italy": "112",
  "Jamaica": "113",
  "Jan Mayen": "114",
  "Japan": "115",
  "Jarvis Island": "116",
  "Jersey": "117",
  "Johnston Atoll": "118",
  "Jordan": "119",
  "Juan de Nova Island": "120",
  "Kazakhstan": "121",
  "Kenya": "122",
  "Kiribati": "123",
  "Korea, North": "124",
  "Korea, South": "125",
  "Kuwait": "126",
  "Kyrgyzstan": "127",
  "Laos": "128",
  "Latvia": "129",
  "Lebanon": "130",
  "Lesotho": "131",
  "Liberia": "132",
  "Libya": "133",
  "Liechtenstein": "134",
  "Lithuania": "135",
  "Luxembourg": "136",
  "Macau": "137",
  "Macedonia, Former Yugoslav Republic of": "138",
  "Madagascar": "139",
  "Malawi": "140",
  "Malaysia": "141",
  "Maldives": "142",
  "Mali": "143",
  "Malta": "144",
  "Man, Isle of": "145",
  "Marshall Islands": "146",
  "Martinique": "147",
  "Mauritania": "148",
  "Mauritius": "149",
  "Mayotte": "150",
  "Mexico": "151",
  "Micronesia, Federated States of": "152",
  "Midway Islands": "153",
  "Moldova": "154",
  "Monaco": "155",
  "Mongolia": "156",
  "Montserrat": "157",
  "Morocco": "158",
  "Mozambique": "159",
  "Namibia": "160",
  "Nauru": "161",
  "Nepal": "162",
  "Netherlands": "163",
  "Netherlands Antilles": "164",
  "New Caledonia": "165",
  "New Zealand": "166",
  "Nicaragua": "167",
  "Niger": "168",
  "Nigeria": "169",
  "Niue": "170",
  "Norfolk Island": "171",
  "Northern Mariana Islands": "172",
  "Norway": "173",
  "Oman": "174",
  "Pakistan": "175",
  "Palau": "176",
  "Panama": "177",
  "Papua New Guinea": "178",
  "Paraguay": "179",
  "Peru": "180",
  "Philippines": "181",
  "Pitcaim Islands": "182",
  "Poland": "183",
  "Portugal": "184",
  "Puerto Rico": "185",
  "Qatar": "186",
  "Reunion": "187",
  "Romainia": "188",
  "Russia": "189",
  "Rwanda": "190",
  "Saint Helena": "191",
  "Saint Kitts and Nevis": "192",
  "Saint Lucia": "193",
  "Saint Pierre and Miquelon": "194",
  "Saint Vincent and the Grenadines": "195",
  "Samoa": "196",
  "San Marino": "197",
  "Sao Tome and Principe": "198",
  "Saudi Arabia": "199",
  "Scotland": "200",
  "Senegal": "201",
  "Seychelles": "202",
  "Sierra Leone": "203",
  "Singapore": "204",
  "Slovakia": "205",
  "Slovenia": "206",
  "Solomon Islands": "207",
  "Somalia": "208",
  "South Africa": "209",
  "South Georgia and South Sandwich Islands": "210",
  "Spain": "211",
  "Spratly Islands": "212",
  "Sri Lanka": "213",
  "Sudan": "214",
  "Suriname": "215",
  "Svalbard": "216",
  "Swaziland": "217",
  "Sweden": "218",
  "Switzerland": "219",
  "Syria": "220",
  "Taiwan": "221",
  "Tajikistan": "222",
  "Tanzania": "223",
  "Thailand": "224",
  "Tobago": "225",
  "Toga": "226",
  "Tokelau": "227",
  "Tonga": "228",
  "Trinidad": "229",
  "Tunisia": "230",
  "Turkey": "231",
  "Turkmenistan": "232",
  "Tuvalu": "233",
  "Uganda": "234",
  "Ukraine": "235",
  "United Arab Emirates": "236",
  "United Kingdom": "237",
  "Uruguay": "238",
  "USA": "239",
  "Uzbekistan": "240",
  "Vanuatu": "241",
  "Venezuela": "242",
  "Vietnam": "243",
  "Virgin Islands": "244",
  "Wales": "245",
  "Wallis and Futuna": "246",
  "West Bank": "247",
  "Western Sahara": "248",
  "Yemen": "249",
  "Yugoslavia": "250",
  "Zambia": "251",
  "Zimbabwe": "252"
}


const STATE_NAME_TO_ID = {
  "Andaman and Nicobar Islands": "1555",
  "Andhra Pradesh": "1556",
  "Arunachal Pradesh": "1557",
  "Assam": "1558",
  "Bihar": "1559",
  "Chandigarh": "1560",
  "Chhattisgarh": "1561",
  "Dadra and Nagar Haveli": "1562",
  "Daman and Diu": "1563",
  "Delhi": "1564",
  "Goa": "1565",
  "Gujarat": "1566",
  "Haryana": "1567",
  "Himachal Pradesh": "1568",
  "Jammu and Kashmir": "1569",
  "Jharkhand": "1570",
  "Karnataka": "1571",
  "Kerala": "1572",
  "Lakshadweep": "1573",
  "Madhya Pradesh": "1574",
  "Maharashtra": "1575",
  "Manipur": "1576",
  "Meghalaya": "1577",
  "Mizoram": "1578",
  "Nagaland": "1579",
  "Orissa": "1580",
  "Pondicherry": "1581",
  "Punjab": "1582",
  "Rajasthan": "1583",
  "Sikkim": "1584",
  "Tamil Nadu": "1585",
  "Telangana": "1586",
  "Tripura": "1587",
  "Uttar Pradesh": "1588",
  "Uttaranchal": "1589",
  "West Bengal": "1590"
}


function translateCountry(value) {
  if (!value) return value;

  // already numeric ID
  if (/^\d+$/.test(value)) return value;

  return COUNTRY_NAME_TO_ID[value] || "0";
}

function translateState(value) {
  if (!value) return value;

  // already numeric ID
  if (/^\d+$/.test(value)) return value;

  return STATE_NAME_TO_ID[value] || value;
}

function getPriorityData(data){
  priorities=["species","scientific_name","current_name","synonyms","notes"]
  priorities.forEach((item)=>{
    if(data[item].length!=0)
      return data[item]
  })
  return "Not Available"
}



chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action !== "fillForm") return;

  // Delay to ensure DOM + Select2 are ready
  setTimeout(() => {
    const data = message.payload;
    data["country_id"]=data["country_name"]
    data["flag_family"]=0
    data["flag_latitude"]=0
    data["flag_longitude"]=0
    data["flag_altitude"]=0
    data["flag_locality"]=0
    data["flag_village"]=0
    data["flag_city"]=0
    data["flag_state"]=0
    data["flag_acc_number"]=0
    data["flag_collection_date"]=0
    data["flag_collection_number"]=0
    data["flag_collection_collector_name"]=0
    data["flag_author_infra"]=0
    data["flag_infraspecific_taxon"]=0
    data["flag_infraspecific_rank"]=0
    data["flag_author_name"]=0
    data["flag_synonyms"]=0
    data["flag_current_name"]=0
    data["flag_scientific_name"]=0
    data["flag_species"]=0
    data["flag_country"]=0
    
    Object.entries(data).forEach(([id, value]) => {

      // ----- LATITUDE -----
      if (id === "latitude" && value) {
        const match = value.match(/([NS])\s*(\d+)\s*[°]?\s*(\d+)'\s*([\d.]+)/);
        if (match) {
          setValue("lat_dir", match[1]);
          setValue("lat_deg", match[2]);
          setValue("lat_min", match[3]);
          setValue("lat_sec", match[4]);
        }
        return;
      }

      // ----- COUNTRY TRANSLATION -----
      if (id === "country_id") {
        value = translateCountry(value);
        if(value==0){
          value="105"
          data["flag_country"]=1
          setValue("flag_country",1)
        }
      }

      // ----- STATE TRANSLATION -----
      if (id === "state_id") {
        value = translateState(value);
      }


      // ----- LONGITUDE -----
      if (id === "longitude" && value) {
        const match = value.match(/([EW])\s*(\d+)\s*[°]?\s*(\d+)'\s*([\d.]+)/);
        if (match) {
          setValue("lon_dir", match[1]);
          setValue("lon_deg", match[2]);
          setValue("lon_min", match[3]);
          setValue("lon_sec", match[4]);
        }
        return;
      }

      // ----- Check where validation is required
      if(id=="flag_family" && value==0){
        if(data['family'].length==0){
          setValue("family","Not Available")
          value=1
        }
      }

      if(id=="flag_genus" && value==0){
        if(data['genus'].length==0){
          setValue("genus","Not Available")
          value=1
        }
      }

      if(id=="acc_number"){
        value=""
      }
      if(id=="collection_number"){
        value=""
      }
      // ----- NORMAL -----
      setValue(id, value);
    });
  }, 300); // <-- critical
});

// ---------- Helper ----------
function setValue(id, value) {
  const el = document.getElementById(id);
  if (!el) return;

  if (el.type === "checkbox") {
    el.checked = value === 1 || value === true;
  }
  else if (el.tagName === "SELECT") {
    el.value = value;
    el.dispatchEvent(new Event("change", { bubbles: true }));

    // Select2 support
    if (window.jQuery && jQuery(el).hasClass("select2-hidden-accessible")) {
      jQuery(el).trigger("change.select2");
    }
  }
  else {
    el.value = value ?? "";
    el.dispatchEvent(new Event("input", { bubbles: true }));
    el.dispatchEvent(new Event("change", { bubbles: true }));
  }
}


chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

  if (message.action === "submitForm") {
    // Small delay to ensure all values are fully applied
    setTimeout(() => {
      const submitBtn = document.getElementById("submitBtn");

      if (!submitBtn) {
        console.warn("submitBtn not found on page");
        return;
      }

      submitBtn.click();
    }, 300);

    return;
  }

  if (message.action !== "fillForm") return;

  // existing fillForm logic ↓↓↓
});
