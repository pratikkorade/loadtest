import threading
import requests
import json
import concurrent.futures
from subprocess import call
alluser=['9930075128'	,'9967549977','9820139132','9820000564','8898050007','9819586633','9768962805','9810269061','7977279663','9819103939','9821804106','9619095954','9606970090','8779033385','9741130525','9987710525','9930996858','8796622179','9619716888','9820534556','9406887838','9617766336','9821282688','9820527201','9810063186','8565352515','9892040038','8237515024','9619412591','8657197319','8850536611','9867304835','7021749949','9820032125','7057489042','9886385045','9920262026','7021232313','7204635293','8130980013','8073324066','8928460467','8892788712','9537552777','9820610616','8849633950','7760809745','9819666159','9920140864','9073576008','9205366753','7285054706','8072659733','9980408510','8660219990','9975674460','9004179623','9946738045','7984406748','9066674463','9177722040','8130241300','7037973178','9619514323','9867831558','8667039214','9901825252','7208609032','9372032541','7622938812','9921819186','9833850635','9819437376','7021552338','7977956609','7977476797','8777690294','8847350538','8825752893','8054115930','9903606024','8124304212','8968517460','8925133984','9624071121','9769844640','9998249932','9599878556','9311637123','8527750121','9773550331','8799760790','9888311380','7777003897','7433898501','9920131285','7888907447','9674952616','7624833020','7906027853','9172794377','6395368289','7676001997','7602030157','8483948936','8928515964','9514084320','7600800380','7063992382','9582176118','8892919013','9890899316','9011999448','9611045002','8424079574','9082051486','7814560527','8104349113','8754884140','8748061732','8980558421','9987022829','9677276800','9920219999','9971772886','7499845779','9880096717','9999691972','9967490463','7021975901','7022135329','8971741321','7390007627','8816812755','9082015850','6355232300','8433624372','9958388963','7276327029' ,'7736219135','9624599967','6382524280','8861420071','9815938728','9380670252','7982457648','9727861710','9411207824','8200855854','9899557786','9207844842','9987536603','8800689333','8588961226','9176165473','7304864884','9082502898','9997822218','9106118382','7022457891','9768980700','8610026813','9891190549','9870444888','9029135203','9082824276','8745037178','7506895886','6395773879','7698815774','9914986420','8850523828','9971294353','9380070548','9461339083','7872410999','8551030693','8146880908','8800342812','7986424802','8780375993','9004103091','7888598527','7358016313','7053506200','9167692423','9205653593','6353605283','8097783196','9423371052','9820804883','8197223802','7697730038','9372989188','8138958466','6380898233','9537966440','9998929183','8369059187','8454989280'	,'7899444147','7666138171','8800391946','9591235462','9892709390','7276299265','7829482880','7043704431','9167888199','9909430220'  ,'8160935034','9768583873','8849525038','7046617205','7383009503','9501103153','7528866218','9667044291','9560126293','9872713952','9035823671','8169861810','8850056819','8792859738','8920036143','8961530184','9159033550','7016689086','8347016636','9769164733','8610670938','9051364123','9540129777','8196851369','9879837193','9821833065','9953839664','9875411055','9819681669','8296504882','7595973336','8291771605','9815470541','9458279400','8017723396','9867424137','9496185255','7026969467','9819238992','8428898947','9830156655','9870058547','9408023794','9769247979','8447032748','8610579654','9137882491','9377824762','9100707197','8548853262','9265734042','9748141864','9840366235','9731317983','9099982447','9625363035','6355865186','9930081069','7982562715','6352475159','9167957294','9654383476','9867932527','9538426015','9512284426','9978967072','9971198386','9909545946','9987278504','8369037641','9619405416','7066268840','9892935370','9044322405','8336058957','7984041894','7980522915','8810680769','9066211098','7892858763','8920419661','9804027744','7338805899','9582853421','9886960794','6380294204','9481985050','9004131848','7405139327','9790785164','9182446515','9821191013','8355872183','8527639514','7048985180','7483473793','9265549147','7010156711','8851048683','8124444836','9769557278','8860737431','9035627234','7338273091','9903832975','9321426924','8553836359','9599710246','6290407075','9810648723','9438187018','9987788463','9123833498','8153912087','9157659554','8851612518','9159993332','9910363316','8238121812','9167459941','9818912150','8961434315','8097746669','9458490177','9092604992','7022545981','8861358318','9315895502','7977955067','9372104585','8585930350','8777472362','8082748494','9717893200','899658327 ','7700043692','9920977278','9987145272','7506414622','8169527078','6283793328','6290315179','7900191204','6361405359','9821015242','9871048396','9810601898','9717710828','9990654524','7003583535','8848730425','7203899392','9319262120','9205575089','8692903858','8583996540','9167364450','6380115257','8307884173','7651886404','8762897006','9422847919','9892070791','7010180850','9167482439','9892168484','7338713787','9325580298','9106763934','9810535017','8490834683','7840040128','9920973776','9924475800','671651235 ','9082519426','9071172512','9599767928','7021029049','8356860047','9674979778','9884880906','8800282847','9995481575','9599270568','9872373970','9702625286','8451947676','7994355720','9967539772','7986266747','8123936514','8976458859','6352027897','8240513515','6375564409','9901463686','9664662305','9664662306','9664662307','9664662301','976896280','9930075128'	,'9967549977','9820139132','9820000564','8898050007','9819586633','9768962805','9810269061','7977279663','9819103939','9821804106','9619095954','9606970090','8779033385','9741130525','9987710525','9930996858','8796622179','9619716888','9820534556','9406887838','9617766336','9821282688','9820527201','9810063186','8565352515','9892040038','8237515024','9619412591','8657197319','8850536611','9867304835','7021749949','9820032125','7057489042','9886385045','9920262026','7021232313','7204635293','8130980013','8073324066','8928460467','8892788712','9537552777','9820610616','8849633950','7760809745','9819666159','9920140864','9073576008','9205366753','7285054706','8072659733','9980408510','8660219990','9975674460','9004179623','9946738045','7984406748','9066674463','9177722040','8130241300','7037973178','9619514323','9867831558','8667039214','9901825252','7208609032','9372032541','7622938812','9921819186','9833850635','9819437376','7021552338','7977956609','7977476797','8777690294','8847350538','8825752893','8054115930','9903606024','8124304212','8968517460','8925133984','9624071121','9769844640','9998249932','9599878556']
# for u in ['9930075128','9967549977','9820139132','9820000564','8898050007','9819586633','9619611715','9768962805','9810269061','7977279663','8879445051','9819103939','9821804106','9619095954','9606970090','8779033385','8657197316','9876523142','9741130525','9004043075','8928779632','9987710525','9930996858','8796622179','9619716888','8082002354','9820534556','9892307825','8601144138','9768962807','9757140063','9406887838','9617766336','9821282688','7776958612','9820982837','9004380998','9820527201','9810063186','8565352515','9892040038','8237515024','9406888838','9619412591','8617766336','8657197319','8850536611','9867304835','7021749949','9820032125','7057489042','8979456585','9886385045','9058062742','9943255503','8128808835','9920262026','7021232313','7204635293','8130980013','9326852176','7736662774','8073324066','7021203264','8523697419','8928460467','8888888888','8962515582','7827597911','7018557928','8892788712','9372164624','9920093933','9537552777','9711306625','8698145415','9820610616','9512217749','8849633950','7760809745','9821547821','8169039233','9819666159','9820139135','9972041283','9920140864','9073576008','8336854408','8800148759','9205366753','8130076846','7285054706','8072659733','9980408510','8660219990','9975674460','9004179623','9987180159','7037378313','8608747589','9946738045','7984406748','9066674463','8454919046','7838491919','9177722040','8130241300','8124437381','8433720049','7718968195','7065331239','8459701691','8401801354','7986114795','7037973178','9619514323','9867831558','8667039214','9901825252','9444046125','9619396979','9619038676','7208609032','9372032541','7622938812','9921819186','9409252013','9833850635','9998686916','8777293797','8369126473','9819437376','7021552338','7977956609','7977476797','8777690294','7829978829','8497848453','8920901375','8847350538','8825752893','8054115930','9903606024','8124304212','8968517460','9791645076','8925133984','9624071121','9769844640','9998249932','9717321856','9599878556','8446221545','9311637123','8527750121','9265182135','8288897770','9773550331','9574331127','6998777777','8799760790','6290471464','7278531886','7622072084','8830290602','9049156845','9082559674','9372514500','9888311380','8130102275','7738794227','7777003897','9354056839','9974044097','9994895377','7982374768','7433898501','9540140760','8758016424','6397767240','7011146652','9920131285','7888907447','9674952616','9820316763','7624833020','8149988653','7021425390','8758424755','9904545660','8980163469','9359878708','7906027853','9172794377','9873822639','7039312120','6395368289','7676001997','8556865480','6353793626','9620063243','7602030157','8483948936','8928515964','8015150405','9514084320','8377079350','9833416829','7703878518','8767123487','8347227037','7738652174','9911465377','7600800380','7063992382','9582176118','6382082807','7010377592','8010207463','8448831776','8860822822','8892919013','9813036248','9890899316','9011999448','9574137846','7827647087','9667027527','9611045002','8424079574','7003796992','7046559770','6351116170','9082051486','7814560527','8104349113','8754884140','6289045190','7419113166','8851468520','8291196603','9867793226','8748061732','8980558421','9987022829','9677276800','7837431343','9131139655','9920219999','9971772886','7499845779','8296904765','9880096717','9999691972','9712870224','6382793365','7528908315','8146779999','9001069777','9967490463','7982984409','7021975901','7022135329','8971741321','7390007627','8056569299','9167616203','8816812755','9082015850','8053884000','6355232300','8433624372','9643393570','9958388963','9663261188','7483538266','9324171169','9205151065','7276327029','7736219135','9910184910','9624599967','6382524280','8527739739','9811015999','8828260070','8425081829','9773111957','6383672269','9664917353','9899550971','8141499694','8861420071','8369915304','9815938728','9380670252','9603174491','9606174491','9586083537','7982457648','7411994732','9779711284','9727861710','9411207824','8200855854','8754685535','7621042208','6354498542','9899557786','9207844842','9987536603','8420386516','8800689333','8588961226','9503039880','9176165473','7304864884','9082502898','8802166090','9997822218','9106118382','9050909765','7248615004','8609998895','7022457891','8447187207','9768980700','6352531334','9599633179','9318446053','9598193409','7814812765','9445626526','8610026813','6283004496','9891190549','9870444888','9029135203','9082824276','8745037178','7506895886','6395773879','7698815774','7358657776','7838648082','9899738112','6352550071','9914986420','8850523828','8438524250','9971294353','9664662308','9380070548','8780736298','9818159917','9461339083','7872410999','8551030693','8146880908','7666640915','9980115268','9354881065','6362571180','8800342812','7290870902','7986424802','9711591538','8780375993','9004103091','8920249129','7888598527','7358016313','7053506200','9167692423','9558835132','9535567844','8010099077','9205653593','6353605283','8097783196','8850826925','8160156090','9423371052','9820804883','8197223802','7697730038','9136779301','9372989188','8138958466','8968684476','6289218534','9999996559','7506901048','9599459310','9741866608','8488996404','7202976155','8490086660','7982659787','6380898233','9537966440','9284502558','9998929183','8369059187','6356155403','9833269217','8454989280','7899444147','8939246697','7666138171','8800391946','8755609638','6201115396','8160319813','9591235462','8657194319','9860714812','9924066811','9892709390','7276299265','8866931277','7829482880','8838456929','7043704431','9870576523','9167888199','9324013731','9909430220','8160935034','8169093082','7726021891','9748428429','9714198033','9768583873','8652236606','9810259860','8849525038','8447760005','7046617205','8660910683','7383009503','8850762705','8075731389','9662376878','9699968634','9501103153','6363567016','7528866218','9667044291','9163818008','9560126293','9872713952','8097563715','8104976896','9106408565','9035823671','7359228758','8169861810','8850056819','7975675975','7837585758','8059481791','8792859738','8734838399','8920036143','9328275107','8961530184','9803520400','9159033550','7016689086','6352670710','9901448496','8347016636','9769164733','9913669417','8104651204','9172197711','8610670938','6352593507','9051364123','8928669549','9372890397','9540129777','8196851369','9979360342','9879837193','9821833065','9953839664','8754697700','8469050637','9875411055','9819681669','8296504882','7595973336','8291771605','6283012933','9815470541','8754313899','9876665793','7303880496']:    alluser.append(str(u))
# print(len(alluser))
# exit()
def thread_second(Mobile_no):
    call(["python", "load_test.py", Mobile_no])

# def base_call(testName, url, data, action='POST'):
#     headers = {'Content-type': 'application/json'}

#     if action == "GET":
#         r = requests.get(url, headers=headers)
#     else:
#         r = requests.post(url, json.dumps(data), headers=headers)
#     return r

with concurrent.futures.ThreadPoolExecutor(max_workers=len(alluser)) as executor:
		futures = {executor.submit(thread_second, url): url for url in alluser}
		concurrent.futures.wait(futures)
		for future in concurrent.futures.as_completed(futures):
			url = futures[future]
			try:
				data = future.result()
			except Exception as exc:
				print('%r generated an exception: %s' % (url, exc))
			else:
				print('%r page' % (url))