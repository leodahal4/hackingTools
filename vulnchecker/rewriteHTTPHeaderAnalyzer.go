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
  // header
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

func printResult(results [9]map[string]string){
  // printResult
  // This function prints all the results that are obtained from analyze function
  fmt.Println(results)
}

func analyze(val *httpPacket) {
  const standardOutNOTFOUND string = "[NOT FOUND]\t"
  const standardOutFOUND string = "[FOUND]\t"
  var description string
  const redStatus string = "[RED]"
  const greenStatus string = "[GREEN]"
  var vulnerabilityStatus string
  // result := make(map[string]string)
  var resultContainer [9]map[string]string

  parameters := declareParameters()
  XpoweredBy := val.headers.Get(parameters[0])
  if(XpoweredBy == ""){
    description = "\"X-POWERED-BY\"\t NotFound"
    vulnerabilityStatus = greenStatus

    resultContainer[0] = map[string]string{
      "standard": standardOutFOUND,
      "description": description,
      "vulnerabilityStatus": vulnerabilityStatus,
    }

  } else {
    serverName := XpoweredBy
    description = "[\"X-POWERED-BY\" header Found with \" " + serverName + " \".]"
    vulnerabilityStatus = redStatus

    resultContainer[0] = map[string]string{
      "standard": standardOutFOUND,
      "description": description,
      "vulnerabilityStatus": vulnerabilityStatus,
    }

  }

  XXssProtection := val.headers.Get(parameters[1])
  if(XXssProtection == ""){
    description = "X-XSS-Protection header.\tX-XSS-Protection header is either inadequate or missing.The users with the old browsers may be vulnerable to Cross-Site Scripting Attacks."
    vulnerabilityStatus = redStatus

    resultContainer[1] = map[string]string{
      "standard": standardOutNOTFOUND,
      "description": description,
      "vulnerabilityStatus": vulnerabilityStatus,
    }
  } else {
    if(XXssProtection == "1; mode=block") {
      description = "X-XSS-Protection enforced"
      vulnerabilityStatus = greenStatus

      resultContainer[1] = map[string]string{
        "standard": standardOutFOUND,
        "description": description,
        "vulnerabilityStatus": vulnerabilityStatus,
      }
    } else{
      description = "X-XSS-Protection header.\tX-XSS-Protection header is either inadequate or missing.The users with the old browsers may be vulnerable to Cross-Site Scripting Attacks."
      vulnerabilityStatus = redStatus

      resultContainer[1] = map[string]string{
        "standard": standardOutNOTFOUND,
        "description": description,
        "vulnerabilityStatus": vulnerabilityStatus,
      }
    }
  }

  XFrameOptions := val.headers.Get(parameters[2])
  if(XFrameOptions == ""){}
  printResult(resultContainer)
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
