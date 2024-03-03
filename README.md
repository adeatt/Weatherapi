# Weatherapi
A small weather api programm which gives you data about the weather. Currently uses openweathermap but should work with others to.

Modules: requests

It starts by getting the data via the request link and the Api key which is only avaible on the site of the api provider.
Nothing to complicatet it just takes this info puts it into .json and prints it out.

Could be usefull for implementing it with a Access Database.

I did this for a project so yeah. Dont expect much.

Currently working on connecting the API with a Access Database with pyodbc. Encounterd some problems with the Connection. 
When trying to establish a connection it returns a empty List. The wiki says the ACE (Access Engine) is not compatible but idk.
