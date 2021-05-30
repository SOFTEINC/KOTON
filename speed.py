import speedtest  
  
def speed():  
    st = speedtest.Speedtest()
  
    print("download : " + str(st.download()))  
   
  
    print("uplaod : " + str(st.upload()))  


