<template>
    <div>
        <div class="header_">
          <h1>Travels</h1>
          <button class="add" @click="open=!open"><v-icon>mdi-plus</v-icon></button>
        </div>
        <ul>
            <li v-for="travel in travels" :key="travel.code">
                <v-card height="5rem" class="travel-item">
                    <div class="item">
                        <h1>Travel code: {{travel.code}}</h1>
                        <div class="subtitle">
                            <p>Code: {{travel.code}}</p>
                            <p>Status: {{travel.start_time}}</p>
                        </div>
                    </div>
                    <div class="buttons">
                        <buttton class="update"><v-icon>mdi-pencil</v-icon></buttton>
                        <button class="delete" @click="deleteTravel(index=index,code=travel.code)"><v-icon>mdi-delete</v-icon></button>
                    </div>
                </v-card>
            </li>
        </ul>
        <create-travel-modal :open="open"/>
    </div>
</template>

<script>
import createTravelModal from '@/components/createTravelModal.vue';
export default {
  components: { createTravelModal },
    data() {
      return {
        open:false,
        travels: [
        ],
      }
    },
    methods:{
        async getTravels() {
            await fetch(
            'http://127.0.0.1:8000/back/travel',{
                method:"GET",
                mode:'cors',
                headers:{
                "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
                },
                cache:'default'
            }
            ).then((res) => res.json().then(data=> this.travels = data))
        },
        async deleteTravel(index,code){
        this.travels.splice(index,1); //quita elemento de la data local
        await fetch(
        `http://127.0.0.1:8000/back/travel?code=${code}`,{
            method:"DELETE",
            mode:'cors',
            headers:{
              "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
            },
            cache:'default'
          }
        ).then((res) => res.json().then(data => console.log(data) ))
      },
    },
    created(){
        this.getTravels()
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
.travel-item{
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