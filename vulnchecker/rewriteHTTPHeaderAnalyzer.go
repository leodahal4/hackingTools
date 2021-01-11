package main

import (
	"flag"
	"fmt"
	"net/http"
	"os"
)

type httpPacket struct{
  headers http.Header
  response *http.Response
}

func newPacket(thisOne *http.Response) *httpPacket{
  // newPacket()
  //  This function creates a new Packet to be used for
  //  saving the headers obtained
  newPac := httpPacket{thisOne.Header,thisOne}
  return &newPac
}

func declareParameters() [9]string{
  // dedecdeclareParameters()
  // This cunction declares the parameters that are to be checked on the 
  // headear
  var parameters [9]string
  parameters[0] = "x-powered-by"
  parameters[1] = "x-xss-protection"
  parameters[2] = "x-frame-options"
  parameters[3] = "x-content-type-optins"
  parameters[4] = "strict-transport-security"
  parameters[5] = "content-security-policy"
  parameters[6] = "access-control-allow-origin"
  parameters[7] = "x-download-options"
  parameters[8] = "x-permitted-cross-domain-policies"

  // return the parameters
  return parameters

}

func analyze(val *httpPacket) {
  const standardOutNOTFOUND string = "[NOT FOUND]\t"
  const standardOutFOUND string = "[FOUND]\t"

  parameters := declareParameters()
  XpoweredBy := val.headers.Get(parameters[0])
  if(XpoweredBy == ""){
    fmt.Println("\"X-POWERED-BY\"\t NotFound")
  } else {
    fmt.Println(standardOutFOUND + "\"X-POWERED-BY\"\theader Found.\t[Remove]")
  }

  XXssProtection := val.headers.Get(parameters[1])
  if(XXssProtection == ""){
    fmt.Println(standardOutNOTFOUND + "X-XSS-Protection header.\tX-XSS-Protection header is either inadequate or missing.The users with the old browsers may be vulnerable to Cross-Site Scripting Attacks.")
  } else {
    fmt.Println(XXssProtection, " xss header printed")
    if(XXssProtection == "1; mode=block") {
      fmt.Println(standardOutFOUND + "X-XSS-Protection enforced")
    } else{
      fmt.Println(standardOutNOTFOUND + "X-XSS-Protection header.\tX-XSS-Protection header is either inadequate or missing.The users with the old browsers may be vulnerable to Cross-Site Scripting Attacks.")
    }
    fmt.Println("Found XSS")
  }

  XFrameOptions := val.headers.Get(parameters[2])
  if(XFrameOptions == ""){}
}

func initialize(res *http.Response) {
  structVal := newPacket(res)
  fmt.Println("\nStarting analyze process..")
  analyze(structVal)
}

func getHTTPHeaders(url string) {
  fmt.Println("Connecting to the host..")
  response, err := http.Get(url)
  if(err != nil){
    os.Exit(1)
  }
  initialize(response)
}

func main() {
  hostAddress := flag.String("host", "", "host address to analyze (REQUIRED)")
  flag.String("h", "", "Display this message")
  flag.Parse()

  if(*hostAddress == ""){
    flag.PrintDefaults()
    os.Exit(1)
  }

  getHTTPHeaders(*hostAddress)
}
