import requests
city=input('Choose a location to check whats happenig in it:').lower().capitalize()
params = {
    'access_key': '79130944a4f8d07cb86488b3f115297e',
    'query':city
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()
if 'success' in api_response:
    if api_response['success'] == False:
        print(city,' is unavalible')
else:
    print(api_response)
    print('The temperature is',api_response['current']['temperature'],'C,')
    print('Or',round(api_response['current']['temperature'] * 9/5+32),'F.')
    print('The time is',api_response['location']['localtime'][10:],'.')
    weather=api_response['current']['weather_descriptions'][0].replace('[','')
    print('The weather is ',weather,'.')
    if api_response['current']['is_day'] == 'yes':
        print('It is day.')
    else:
        print('it is night.')
    print('the wind direction is',api_response['current']['wind_dir'],'.')
    print('or',api_response['current']['wind_degree'],"degrees.")
    print('it feels like',api_response['current']['feelslike'],'C,')
    print('or',round(api_response['current']['feelslike']* 9/5+32),'F.')