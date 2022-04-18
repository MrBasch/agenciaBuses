<template>
    <div :key="buses.id">
        <div class="header_">
          <h1>Buses</h1>
          <button class="add" @click="open=!open"><v-icon>mdi-plus</v-icon></button>
        </div>
        
        <ul>
            <li v-for="(bus, index) in buses" :key="bus.code">
                <v-card height="5rem" class="bus-item">
                    <div class="item">
                        <h1>Bus code: {{bus.code}}</h1>
                        <div class="subtitle">
                            <p>Status: {{bus.status}}</p>
                        </div>
                    </div>
                    <div class="buttons">
                        <buttton class="update" @click="edit=!edit"><v-icon>mdi-pencil</v-icon></buttton>
                        <button class="delete" @click="deleteBus(index=index,code=bus.code)"><v-icon>mdi-delete</v-icon></button>
                    </div>
                </v-card>
            </li>
        </ul>
        <busModal :key="open" :open="open"/>
        <editBusModal :key="edit" :edit="edit"/>
    </div>
</template>

<script>
import BusModal from '@/components/busModal.vue';
import editBusModal from '@/components/editBusModal.vue';
export default {
    components:{
        BusModal,
        editBusModal,
        },
    data() {
      return {
        open:false,
        edit:false,
        buses: [
        ],
      }
    },
    methods:{
      async deleteBus(index,code){
        this.buses.splice(index,1); //quita elemento de la data local
        await fetch(
        `http://127.0.0.1:8000/back/bus?code=${code}`,{
            method:"DELETE",
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
        ).then((res) => res.json().then(data => this.buses=data))
      },
    },
    created(){
      this.getBuses()
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
.bus-item{
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