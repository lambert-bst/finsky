# Analysis

```java
BASE_URI = Uri.parse((String)"https://android.clients.google.com/fdfe/");
```

Responses can be parsed as `Response.ResponseWrapper` protobuf messages.

## details

Example request:

```
https://android.clients.google.com/fdfe/details
  ?doc=com.netflix.mediaclient
```

Here `doc` is the app ID.

## delivery

Example request:

```
https://android.clients.google.com/fdfe/delivery
  ?doc=com.facebook.katana
  &ot=1
  &st=<removed>
  &vc=10742937
  &bvc=10120647
  &pf=1
  &pf=2
  &ch=ijxLJi1yGs1JpL-X1SExmchvork
```

Java code:

```java
public Request<?> delivery(String string, int n, byte[] arrby, Integer n2, Integer n3, String[] arrstring, String string2, String string3, String string4, Response.Listener<Delivery.DeliveryResponse> listener, Response.ErrorListener errorListener) {
    Uri.Builder builder = DELIVERY_URI.buildUpon().appendQueryParameter("doc", string).appendQueryParameter("ot", Integer.toString(n));
    if (arrby != null) {
        builder.appendQueryParameter("st", DfeApiImpl.base64EncodeToken(arrby));
    }
    if (n2 != null) {
        builder.appendQueryParameter("vc", n2.toString());
    }
    if (n3 != null) {
        builder.appendQueryParameter("bvc", n3.toString());
        if (arrstring != null) {
            int n4 = arrstring.length;
            for (int i = 0; i < n4; ++i) {
                builder.appendQueryParameter("pf", arrstring[i]);
            }
        }
    }
    if (!TextUtils.isEmpty((CharSequence)string2)) {
        builder.appendQueryParameter("shh", string2);
    }
    if (!TextUtils.isEmpty((CharSequence)string3)) {
        builder.appendQueryParameter("ch", string3);
    }
    if (!TextUtils.isEmpty((CharSequence)string4)) {
        builder.appendQueryParameter("dtok", string4);
    }
    DfeRequest<Delivery.DeliveryResponse> dfeRequest = new DfeRequest<Delivery.DeliveryResponse>(builder.build().toString(), this.mApiContext, Delivery.DeliveryResponse.class, listener, errorListener);
    dfeRequest.setShouldCache(false);
    dfeRequest.setIncludeCheckinConsistencyToken();
    return this.mQueue.add(dfeRequest);
}
```

Response:

```
payload {
  deliveryResponse {
    appDeliveryData {
      downloadSize: 43789085
      signature: "BMSpG6ZA78Pvx1S64U0Akho2Ui8"
      downloadUrl: "https://android.clients.google.com/market/download/Download?packageName=com.facebook.katana&versionCode=11209847&ssl=1&token=AOTCm0SqOMo2UUtgzvqf5ET5NowBb9xuPK1JP5Tq59DD1LLzSE9e35fsPasoOi7sYOBdU8F32ugK8_yelE15er9Q7LYyL40KdtKlDE5RCvmDAE2Wic7W5V3WvwPzvTGgfpLLllnX6F5fRPaBCjOVMFT8p6b7kQ6m3Y7O3D2FLvvMQpLR7F25byLg-yGGhcI_BSbkyYlT6-4yzIqcD37waYBKWxrVCpvF&downloadId=-1748287373119731515"
      downloadAuthCookie {
        name: "MarketDA"
        value: "04273586160470978360"
      }
      forwardLocked: false
      serverInitiated: true
      gzippedDownloadUrl: "https://android.clients.google.com/market/download/Download?packageName=com.facebook.katana&versionCode=11209847&ssl=1&token=AOTCm0RkmHvburjlSE3voAleZFjnjteHS4-icK9Ct8RMhvfvsHLERZIxN75QAJRMdltFOLTKZMpBKDjzXMOrIE_AuZNMubLiBR3GwflRHR6akCJ6bjOfEHNjRjyVKk7QxY3r5WW_tAMtgYxUNARwvdS9q1d7jTuNM7kU6fZf8woIFMuyE13hTcGkjVmcUqQoIPAxKYem8dP3hdl_-GD40hqqyYaiCSYH&downloadId=-1748287373119731515&gz=1"
      gzippedDownloadSize: 39609985
      installLocation: 2
    }
  }
}
serverMetadata {
  latencyMillis: 636
}
```