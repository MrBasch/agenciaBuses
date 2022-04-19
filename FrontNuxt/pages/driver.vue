<template>
    <div>
        <div class="header_">
          <h1>Driver</h1>
          <button class="add" @click="open=!open"><v-icon>mdi-plus</v-icon></button>
        </div>
        
        <ul>
            <li v-for="(driver, index) in drivers" :key="driver.rut">
                <v-card height="5rem" class="item_card">
                    <div class="item">
                        <h1>Name: {{driver.name}}</h1>
                        <div class="subtitle">
                            <p>Rut: {{driver.rut}}</p>
                        </div>
                    </div>
                    <div class="buttons">
                        <buttton class="update" @click="edit=!edit"><v-icon>mdi-pencil</v-icon></buttton>
                        <button class="delete" @click="deleteDriver(rut=driver.rut,index=index)"><v-icon>mdi-delete</v-icon></button>
                    </div>
                </v-card>
            </li>
        </ul>
        <createDriverModal :key="open" :open="open"/>
        <updateDriverModal :key="edit" :edit="edit"/>
    </div>
</template>

<script>
import createDriverModal from '@/components/createDriverModal.vue';
import updateDriverModal from '@/components/updateDriverModal.vue';

export default {
    components:{
        createDriverModal,updateDriverModal
        },
    data() {
      return {
        open:false,
        edit:false,
        drivers: [
        ],
      }
    },
    methods:{
        async deleteDriver(rut,index){
            this.drivers.splice(index,1); //quita elemento de la data local
            await fetch(
            `http://127.0.0.1:8000/back/driver?rut=${rut}`,{
                method:"DELETE",
                mode:'cors',
                headers:{
                "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
                },
                cache:'default'
            }
            ).then((res) => res.json().then(data => console.log(data) ))
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
            ).then((res) => res.json().then(data =>{
                console.log("data =",data)
                return this.drivers=data
            }))
        },
    },
    created(){
      this.getDrivers()
    },
    
}
</script>

<style scoped>

ul {
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.subtitle{
  display: flex;
  gap:0.8rem
}
h1, p, .v-icon{
  color: #021C36;
}
.item{
  margin-left: 1rem;
    
}
.item_card{
  display: flex;
  justify-content: space-between;
  background-color: #EDE6DB;
}
.buttons{
  display: flex;
  align-items: center;
  padding-right: 1rem;
}
</style>