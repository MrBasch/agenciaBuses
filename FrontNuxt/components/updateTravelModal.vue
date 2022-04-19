<template>
  <v-dialog max-width="500px" v-model="edit" >
    <v-card class="addDialog">
      <v-card-title>Update or create travel</v-card-title>
      <v-form>
        <v-text-field v-model="code" label="Enter travel code"></v-text-field>
        <v-text-field v-model="new_code" label="Enter new travel code"></v-text-field>
        <v-text-field v-model="start_time" label="Enter travel start time" placeholder="2022-02-04 11:30:45"></v-text-field>
        <v-text-field v-model="end_time" label="Enter travel end time" placeholder="2022-02-05 12:30:45"></v-text-field>
        <v-select v-model="rut_driver" :items="drivers" label="Select a driver"></v-select>
        <v-select v-model="code_bus" :items="buses" label="Select a bus"></v-select>
        <v-select v-model="code_route" :items="routes" label="Select a route"></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click.stop="updateTravel(code=code,new_code=new_code,code_route=code_route,start_time=start_time,end_time=end_time,rut_driver=rut_driver,code_bus=code_bus)" color="green">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name:'updateTravelModal',
  props:['edit'],
  data() {
    return {
      code:"",
      new_code:'',
      state: "",
      start_time:'',
      end_time:'',
      rut_driver:'',
      code_bus:'',
      code_route:'',
      drivers:[],
      buses: [],
      routes:[],
    };
  },
  methods:{
    async updateTravel(code,new_code,code_route,start_time,end_time,rut_driver,code_bus){
        console.log("code = ", code ,"code_route =", code_route, "starttime=", start_time, "end_time = ", end_time, "rut_driver =",rut_driver, "code_bus = ", code_bus)
        await fetch(
        `http://127.0.0.1:8000/back/travel?code=${code}&new_code=${new_code}&route=${code_route}&start_time=${start_time}&end_time=${end_time}&rut_driver=${rut_driver},&code_bus=${code_bus}`,{
            method:"PUT",
            mode:'cors',
            headers:{
              "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
            },
            cache:'default'
          }
        ).then((res) => res.json().then(data => console.log(data) ))
      },
      async getBuses() {
        await fetch(
        'http://127.0.0.1:8000/back/bus',{
            method:"GET",
            mode:'cors',
            headers:{
              "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
            },
            cache:'default'
          }
        ).then((res) => res.json().then(data => { 
            data.map(bus => this.buses.push(bus.code))}
        ))
      },
      async getDrivers() {
        await fetch(
        'http://127.0.0.1:8000/back/driver',{
            method:"GET",
            mode:'cors',
            headers:{
              "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
            },
            cache:'default'
          }
        ).then((res) => res.json().then(data => { 
            data.map(driver => this.drivers.push(driver.rut))}
        ))
      },
      async getRoutes() {
        await fetch(
        'http://127.0.0.1:8000/back/route',{
            method:"GET",
            mode:'cors',
            headers:{
              "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
            },
            cache:'default'
          }
        ).then((res) => res.json().then(data => { 
            data.map(route => this.routes.push(route.code))}
        ))
      },
  },
  created(){
      this.getBuses()
      this.getDrivers()
      this.getRoutes()
  }
}
</script>
<style scoped>
.addDialog{
  overflow: hidden;
  background-color: #8b8070;
}
</style>