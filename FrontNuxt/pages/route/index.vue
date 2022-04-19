<template>
    <div>
        <div class="header_">
          <h1>Routes</h1>
          <button class="add" @click="open=!open"><v-icon>mdi-plus</v-icon></button>
        </div>
        <ul>
            <li v-for="(route, index) in routes" :key="route.code">
                <v-card height="5rem" class="item_card">
                    <div class="item">
                        <h1>Route name: {{route.name}}</h1>
                        <div class="subtitle">
                            <p>Code: {{route.code}}</p>
                            <p>Status: {{route.status}}</p>
                        </div>
                    </div>
                    <div class="buttons">
                        <buttton class="update" @click="edit=!edit"><v-icon>mdi-pencil</v-icon></buttton>
                        <button class="delete" @click="deleteRoute(index=index,code=route.code)"><v-icon>mdi-delete</v-icon></button>
                    </div>
                </v-card>
            </li>
        </ul>
        <create-route-modal :open="open"/>
        <update-route-modal :edit="edit"/>
    </div>
</template>

<script>
import CreateRouteModal from '@/components/createRouteModal.vue';
import UpdateRouteModal from '@/components/updateRouteModal.vue';
// import updateTravelModal from '@/components/updateTravelModal.vue';
export default {
  components: {CreateRouteModal,UpdateRouteModal },
    data() {
    return {
        edit:false,
        open:false,
        routes: [
        ],
      }
    },
    methods:{
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
            ).then((res) => res.json().then(data=> {
                console.log("data =", data)
                return this.routes = data
            }))
        },
        async deleteRoute(index,code){
            this.routes.splice(index,1); //quita elemento de la data local
            await fetch(
            `http://127.0.0.1:8000/back/route?code=${code}`,{
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
        this.getRoutes()
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