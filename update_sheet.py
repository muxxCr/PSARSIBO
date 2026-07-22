import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
# ======================================
# ENTER YOUR STOCKS HERE
# ======================================

stocks = [
'20MICRONS.NS',
'3MINDIA.NS',
'AGI.NS',
'AWFIS.NS',
'AWL.NS',
'ABB.NS',
'ATGL.NS',
'ADFFOODS.NS',
'ADOR.NS',
'ADVENZYMES.NS',
'AEGISLOG.NS',
'AEROENTER.NS',
'AFFLE.NS',
'AJAXENGG.NS',
'APLLTD.NS',
'ALIVUS.NS',
'ALKYLAMINE.NS',
'ARE&M.NS',
'AMBER.NS',
'AMBIKCO.NS',
'AMBUJACEM.NS',
'AMNPLST.NS',
'ANANTRAJ.NS',
'ANTELOPUS.NS',
'APARINDS.NS',
'APCOTEXIND.NS',
'APLAPOLLO.NS',
'APOLLOHOSP.NS',
'APOLLOTYRE.NS',
'ARTEMISMED.NS',
'ARVINDFASN.NS',
'ARVIND.NS',
'ARVSMART.NS',
'ASHAPURMIN.NS',
'ASIANENE.NS',
'ASIANPAINT.NS',
'ASTERDM.NS',
'ASTRAL.NS',
'ATULAUTO.NS',
'ATUL.NS',
'AUROPHARMA.NS',
'AUTOAXLES.NS',
'ASAL.NS',
'AVALON.NS',
'AVTNPL.NS',
'AZAD.NS',
'BALAMINES.NS',
'BALMLAWRIE.NS',
'BERGEPAINT.NS',
'BEPL.NS',
'BHARATSE.NS',
'BIRLACORPN.NS',
'BLISSGVS.NS',
'BLS.NS',
'BLUESTARCO.NS',
'BBTC.NS',
'BOROSCI.NS',
'BOSCHLTD.NS',
'BUTTERFLY.NS',
'CGPOWER.NS',
'CIEINDIA.NS',
'CAPLIPOINT.NS',
'CARTRADE.NS',
'CARYSIL.NS',
'CEATLTD.NS',
'CEMPRO.NS',
'CENTURYPLY.NS',
'CLSEL.NS',
'COALINDIA.NS',
'CONFIPET.NS',
'COSMOFIRST.NS',
'CRAFTSMAN.NS',
'MUFTI.NS',
'CUMMINSIND.NS',
'DDEVPLSTIK.NS',
'DCMSHRIRAM.NS',
'DCW.NS',
'DBEIL.NS',
'DEEPAKNTR.NS',
'DHANUKA.NS',
'DIACABS.NS',
'DIFFNKG.NS',
'DIVISLAB.NS',
'DODLA.NS',
'DOLLAR.NS',
'AGARWALEYE.NS',
'DREDGECORP.NS',
'DWARKESH.NS',
'DYCL.NS',
'EMIL.NS',
'ELGIEQUIP.NS',
'EMCURE.NS',
'ENDURANCE.NS',
'ENTERO.NS',
'EUREKAFORB.NS',
'EVEREADY.NS',
'EKC.NS',
'NYKAA.NS',
'FAZE3Q.NS',
'FIEMIND.NS',
'FINEORG.NS',
'FLAIR.NS',
'FORTIS.NS',
'GVT&D.NS',
'GHCLTEXTIL.NS',
'GMMPFAUDLR.NS',
'GPTHEALTH.NS',
'GABRIEL.NS',
'GALAPREC.NS',
'GALLANTT.NS',
'GANDHAR.NS',
'GRWRHITECH.NS',
'GENUSPOWER.NS',
'GILLETTE.NS',
'GLAND.NS',
'MEDANTA.NS',
'GPIL.NS',
'GOKULAGRO.NS',
'GOODLUCK.NS',
'GOPAL.NS',
'GPTINFRA.NS',
'GRANULES.NS',
'GRAUWEIL.NS',
'GREENLAM.NS',
'GREENPLY.NS',
'GRINDWELL.NS',
'GUFICBIO.NS',
'GUJALKALI.NS',
'GAEL.NS',
'GIPCL.NS',
'GNFC.NS',
'GPPL.NS',
'HFCL.NS',
'HAPPYFORGE.NS',
'HARIOMPIPE.NS',
'HAVELLS.NS',
'HSCL.NS',
'HINDCOPPER.NS',
'POWERINDIA.NS',
'HONASA.NS',
'IFGLEXPOR.NS',
'IKIO.NS',
'IFBIND.NS',
'IGPL.NS',
'IPL.NS',
'IOC.NS',
'INDIGOPNTS.NS',
'INDRAMEDCO.NS',
'INDUSTOWER.NS',
'INOXGREEN.NS',
'IGIL.NS',
'IKS.NS',
'IOLCP.NS',
'IRB.NS',
'JGCHEM.NS',
'JSWDULUX.NS',
'JTEKTINDIA.NS',
'JTLIND.NS',
'JAMNAAUTO.NS',
'JASH.NS',
'JAYBARMARU.NS',
'JAYAGROGN.NS',
'JSL.NS',
'JINDALSTEL.NS',
'JKPAPER.NS',
'JUBLINGREA.NS',
'JLHL.NS',
'KPEL.NS',
'KPRMILL.NS',
'KPIGREEN.NS',
'KRN.NS',
'KAJARIACER.NS',
'KCP.NS',
'KEI.NS',
'KERNEX.NS',
'KINGFA.NS',
'KIRLFER.NS',
'KIRLPNU.NS',
'KOPRAN.NS',
'KROSS.NS',
'KRSNAA.NS',
'LMW.NS',
'LANDMARK.NS',
'LAURUSLABS.NS',
'LAXMIDENTL.NS',
'IXIGO.NS',
'LLOYDSME.NS',
'LODHA.NS',
'LUMAXIND.NS',
'LUPIN.NS',
'MMP.NS',
'MTARTECH.NS',
'MBAPL.NS',
'MCLOUD.NS',
'MAHLOG.NS',
'MANGLMCEM.NS',
'MARINE.NS',
'MARKSANS.NS',
'MAXHEALTH.NS',
'MAYURUNIQ.NS',
'MEDPLUS.NS',
'MENONBE.NS',
'METROPOLIS.NS',
'MINDACORP.NS',
'MIDHANI.NS',
'MOLDTKPAC.NS',
'MSUMI.NS',
'MRF.NS',
'NDRAUTO.NS',
'NIITMTS.NS',
'NSLNISP.NS',
'NAHARINDUS.NS',
'NH.NS',
'NFL.NS',
'NAVINFLUOR.NS',
'NAVKARCORP.NS',
'NEOGEN.NS',
'NESTLEIND.NS',
'NEULANDLAB.NS',
'NILKAMAL.NS',
'NRBBEARING.NS',
'OBEROIRLTY.NS',
'ONGC.NS',
'OLECTRA.NS',
'OPTIEMUS.NS',
'ORCHPHARMA.NS',
'ORIENTCEM.NS',
'ORIENTELEC.NS',
'OSWALPUMPS.NS',
'PSPPROJECT.NS',
'PTCIL.NS',
'PANAMAPET.NS',
'PARAGMILK.NS',
'PARACABLES.NS',
'PGIL.NS',
'PENIND.NS',
'PETRONET.NS',
'PLATIND.NS',
'POLYCAB.NS',
'POLYPLEX.NS',
'POCL.NS',
'PRAKASH.NS',
'PPL.NS',
'PREMIERENE.NS',
'PRESTIGE.NS',
'PRICOLLTD.NS',
'PRINCEPIPE.NS',
'PURVA.NS',
'PYRAMID.NS',
'QUESS.NS',
'RRKABEL.NS',
'RPEL.NS',
'RAILTEL.NS',
'RAINBOW.NS',
'RAMRAT.NS',
'RAMCOIND.NS',
'RAMCOSYS.NS',
'RANEHOLDIN.NS',
'RPTECH.NS',
'RCF.NS',
'RATNAVEER.NS',
'RELTD.NS',
'REFEX.NS',
'RELAXO.NS',
'ROSSARI.NS',
'ROUTE.NS',
'RUPA.NS',
'SCHAND.NS',
'SJS.NS',
'SMLMAH.NS',
'SRM.NS',
'SAILIFE.NS',
'MOTHERSON.NS',
'SANDHAR.NS',
'SANGHVIMOV.NS',
'SANOFICONR.NS',
'SANSERA.NS',
'SANSTAR.NS',
'SOTL.NS',
'SEAMECLTD.NS',
'SIS.NS',
'SENORES.NS',
'SHAILY.NS',
'SHALBY.NS',
'SHARDACROP.NS',
'SFL.NS',
'SHILPAMED.NS',
'SBCL.NS',
'SHRIPISTON.NS',
'SHRIRAMPPS.NS',
'SHYAMMETL.NS',
'SIGNATURE.NS',
'SILVERTUC.NS',
'SIRCA.NS',
'SIYSIL.NS',
'SKIPPER.NS',
'SOBHA.NS',
'SOLARINDS.NS',
'SOMANYCERA.NS',
'SONACOMS.NS',
'SPECTRUM.NS',
'SRF.NS',
'SETL.NS',
'STARCEMENT.NS',
'SAIL.NS',
'SSWL.NS',
'STLTECH.NS',
'STYRENIX.NS',
'SUBROS.NS',
'SUDARSCHEM.NS',
'SUDARCOLOR.NS',
'SUKHJITS.NS',
'SUMICHEM.NS',
'SUNDRMFAST.NS',
'SUPRAJIT.NS',
'SUPREMEIND.NS',
'SPLPETRO.NS',
'SBGLP.NS',
'SWANCORP.NS',
'SYRMA.NS',
'TATACONSUM.NS',
'TVSSCS.NS',
'TALBROAUTO.NS',
'TNPL.NS',
'TANLA.NS',
'TDPOWERSYS.NS',
'TIIL.NS',
'TEXRAIL.NS',
'PHOENIXLTD.NS',
'THEJO.NS',
'THERMAX.NS',
'TIMETECHNO.NS',
'TITAGARH.NS',
'TCI.NS',
'TRITURBINE.NS',
'TTKPRESTIG.NS',
'TVSSRICHAK.NS',
'ULTRACEMCO.NS',
'UNIPARTS.NS',
'UNOMINDA.NS',
'USHAMART.NS',
'VADILALIND.NS',
'VAIBHAVGBL.NS',
'VALIANTORG.NS',
'VSSL.NS',
'VARROC.NS',
'VBL.NS',
'VERANDA.NS',
'VIDHIING.NS',
'VIJAYA.NS',
'VIMTALABS.NS',
'VINATIORGA.NS',
'VINCOFE.NS',
'VISHNU.NS',
'VIYASH.NS',
'VRAJ.NS',
'WAAREEENER.NS',
'WAAREERTL.NS',
'WHEELS.NS',
'WOCKPHARMA.NS',
'WONDERLA.NS',
'XPROINDIA.NS',
'YATHARTH.NS',
'ZFCVINDIA.NS',
'ZYDUSLIFE.NS',
'EMUDHRA.NS',
 'ZYDUSLIFE.NS'
]
# ======================================
# RSI FUNCTION
# ======================================

def calculate_rsi(close, period=14):

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1/period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, adjust=False).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))

# ======================================
# PARABOLIC SAR ON RSI
# ======================================

def sar_on_rsi(rsi, step=0.01, max_af=0.20):

    rsi = rsi.reset_index(drop=True)

    n = len(rsi)

    sar = np.zeros(n)
    trend = np.zeros(n)

    sar[0] = rsi.iloc[0]

    if rsi.iloc[1] >= rsi.iloc[0]:
        trend[0] = 1
        ep = rsi.iloc[1]
    else:
        trend[0] = -1
        ep = rsi.iloc[1]

    af = step

    for i in range(1, n):

        if trend[i-1] == 1:

            sar[i] = sar[i-1] + af * (ep - sar[i-1])

            if rsi.iloc[i] < sar[i]:
                trend[i] = -1
                sar[i] = ep
                ep = rsi.iloc[i]
                af = step
            else:
                trend[i] = 1
                if rsi.iloc[i] > ep:
                    ep = rsi.iloc[i]
                    af = min(af + step, max_af)

        else:

            sar[i] = sar[i-1] - af * (sar[i-1] - ep)

            if rsi.iloc[i] > sar[i]:
                trend[i] = 1
                sar[i] = ep
                ep = rsi.iloc[i]
                af = step
            else:
                trend[i] = -1
                if rsi.iloc[i] < ep:
                    ep = rsi.iloc[i]
                    af = min(af + step, max_af)

    return sar

# ======================================
# SCANNER
# ======================================

results = []

for stock in stocks:

    print(f"Scanning {stock}")

    try:

        df = yf.download(
            stock,
            period="6mo",
            interval="1d",
            auto_adjust=True,
            progress=False
        )

        if len(df) < 50:
            continue

        close = df["Close"].squeeze()

        df["RSI"] = calculate_rsi(close)
        df.dropna(inplace=True)

        df["SAR_RSI"] = sar_on_rsi(df["RSI"])

        prev_rsi = df["RSI"].iloc[-2]
        prev_sar = df["SAR_RSI"].iloc[-2]

        curr_rsi = df["RSI"].iloc[-1]
        curr_sar = df["SAR_RSI"].iloc[-1]

        if prev_rsi < prev_sar and curr_rsi > curr_sar:
            signal = "BUY"
        elif prev_rsi > prev_sar and curr_rsi < curr_sar:
            signal = "SELL"
        else:
            signal = ""

        trend = "Bullish" if curr_rsi > curr_sar else "Bearish"

        results.append({
            "Stock": stock,
            "Previous RSI": round(prev_rsi, 2),
            "Previous SAR": round(prev_sar, 2),
            "Current RSI": round(curr_rsi, 2),
            "Current SAR": round(curr_sar, 2),
            "Trend": trend,
            "Signal": signal
        })

    except Exception as e:
        print(stock, "Error:", e)
# ======================================
# GOOGLE SHEETS
# ======================================

creds_json = os.environ.get("GCP_CREDENTIALS")
creds_dict = json.loads(creds_json)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Replace with your Google Sheet ID
spreadsheet_id = "1M-Vtk5L5v_qYmAXOTgbRA-HKNDeRkip_EA67H8q7uSY"

worksheet = client.open_by_key(spreadsheet_id).worksheet("halal stocks")

# Clear old data
worksheet.clear()

# Upload headers
worksheet.append_row(result_df.columns.tolist())

# Upload data
worksheet.update(
    f"A2:G{len(result_df)+1}",
    result_df.values.tolist()
)

print("Google Sheet Updated Successfully")


