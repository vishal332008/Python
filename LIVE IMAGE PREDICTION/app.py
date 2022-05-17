import { StatusBar } from 'expo-status-bar';
import { Platform, StyleSheet, Text, View, Button } from 'react-native';
import {Permissions} from 'expo-permissions';
import { Component } from 'react';

export default class App extends Component{

  async _getPermissionsAsync(){
    if(Platform.OS!="web"){
      const {status} = await Permissions.askAsync(Permissions.CAMERA_ROLL);
      if(status!="granted"){
        alert("Sorry , we need camera roll permissions to make this work!");
      }
    }
  }
  async uploadImage(uri){
    const data = new FormData();
    let filename = uri.split("/")[uri.split("/").length - 1]
    let type = `image/${uri.split('.')[uri.split('.').length - 1]}`
    const fileToUpload = {
      uri:uri,
      name:filename,
      type:type
    }
    data.append("digit",fileToUpload);
    fetch("https://f292a3137990.ngrok.io/predict-digit",{
      method:"POST",
      body:data,
      headers:{"content-type":"multipart/form-data"}
  
    })
    .then((response) => response.json())
    .then((result) => {
      console.log("Success:",result);
    })
    .catch((error) => {
      console.log("Error:",error)
    })
  }
  return (){
    <View style={styles.container}>
      <Button title="Press me first " onPress={() => this._getPermissionsAsync()} />
      <Button title="Press me next" onPress={() => this.uploadImage()} />
      <StatusBar style="auto" />
    </View>
  };
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
