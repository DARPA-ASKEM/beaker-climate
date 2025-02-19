Overview
The National Weather Service (NWS) API allows developers access to critical forecasts, alerts, and observations, along with other weather data. The API was designed with a cache-friendly approach that expires content based upon the information life cycle. The API is based upon of JSON-LD to promote machine data discovery.

The API is located at: https://api.weather.gov

Operational issues should be reported to nco.ops@noaa.gov.

General use questions can be asked on the API github site.

Pricing
All of the information presented via the API is intended to be open data, free to use for any purpose. As a public service of the United States Government, we do not charge any fees for the usage of this service, although there are reasonable rate limits in place to prevent abuse and help ensure that everyone has access. The rate limit is not public information, but allows a generous amount for typical use. If the rate limit is execeed a request will return with an error, and may be retried after the limit clears (typically within 5 seconds). Proxies are more likely to reach the limit, whereas requests directly from clients are not likely.

Content Negotiation
The new API will use headers to modify the version and format of the response. Every request, either by browser or application, sends header information every time you visit any website. For example, a commonly used header called "UserAgent" tells a website what type of device you are using so it can tailor the best experience for you. No private information is shared in a header, and this is a standard practice for all government and private sites. Developers can override these headers for specific purposes (see the "API Specifications" tab for more information). You can get full details by visiting the header field definitions page at the World Wide Web Consortium site.

Authentication
Format the response
Request new features
Authentication
A User Agent is required to identify your application. This string can be anything, and the more unique to your application the less likely it will be affected by a security event. If you include contact information (website or email), we can contact you if your string is associated to a security event. This will be replaced with an API key in the future.

User-Agent: (myweatherapp.com, contact@myweatherapp.com)
Formats
Endpoints typically have a GeoJSON default format, given the inclusion of geometry data. See the Specification tab for details on each endpoint. Below are common formats available by the API.

GeoJSON: application/geo+json
JSON-LD: application/ld+json
DWML: application/vnd.noaa.dwml+xml
OXML: application/vnd.noaa.obs+xml
CAP: application/cap+xml
ATOM: application/atom+xml
Accept: application/cap+xml
Features
The API will use feature flags to make new features available to consumers. The available feature flags will be noted on the "Updates" and "Specification" tabs on this page. The feature flag will be communicated through a Service Change Notice (SCN) allowing developers a period to adopt the flag if the change impacts their applications. Once the adoption window expires, the feature will be made default. Developers can then remove the flag at their convenience.

Feature-Flags: forecast_temperature_qv
Outage Information
Information on outages is generally communicated through Administrative messages sent by National Center of Environmental Prediction's (NCEP's) Senior Duty Meteorologist (SDM). These are sent via WMO id NOUS42 KWNO and product identifier ADASDM.

Examples of using the API
The API uses linked data to allow applications to discover content. Similar to a web site that provides HTML links to help users navigate to each page, linked data helps applications navigate to each endpoint. You may also review the OPEN API specification on the "Specification" tab on this page, or directly using the specification endpoint (that is also used to create the tab presentation): https://api.weather.gov/openapi.json.

How do I get the forecast?
Forecasts are created at each NWS Weather Forecast Office (WFO) on their own grid definition, at a resolution of about 2.5km x 2.5km. The API endpoint for the 12h forecast periods at a specific grid location is formatted as:

	https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast
For example: https://api.weather.gov/gridpoints/TOP/31,80/forecast

To obtain the grid forecast for a point location, use the /points endpoint to retrieve the current grid forecast endpoint by coordinates:

	https://api.weather.gov/points/{latitude},{longitude}
For example: https://api.weather.gov/points/39.7456,-97.0892

This will provide the grid forecast endpoints for three format options in these properties:

forecast - forecast for 12h periods over the next seven days
forecastHourly - forecast for hourly periods over the next seven days
forecastGridData - raw forecast data over the next seven days
Note: at this time coastal marine grid forecasts are only available from the forecastGridData property.

Applications may cache the grid for a location to improve latency and reduce the additional lookup request; however, it is important to note that while it generally does not occur often, the gridX and gridY values (and even the office) for a given coordinate may occasionally change. For this reason, it is necessary to check back to the /points endpoint periodically for the latest office/grid mapping.

The /points endpoint also contains information about the issuing office, observation stations, and zones for a given point location.

For NOAA Climate Data Online or other NOAA API's, if you need an API token it will be available in the environment variable NOAA_API_KEY.