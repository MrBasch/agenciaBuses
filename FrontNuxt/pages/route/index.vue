<template>
  <div>
    <div class="header_">
      <h1>Routes</h1>
      <div class="buttons_header">
        <button class="add" @click="open = !open">
          <v-icon>mdi-plus</v-icon>
        </button>
        <buttton class="update" @click="edit = !edit">
          <v-icon>mdi-pencil</v-icon>
        </buttton>
      </div>
    </div>
    <ul>
      <li v-for="(route, index) in routes" :key="route.code">
        <v-card height="5rem" class="item_card">
          <div class="item">
            <nuxt-link :to="'/route/' + route.code">
              <h1>Route name: {{ route.name }}</h1>
            </nuxt-link>
            <div class="subtitle">
              <p>Code: {{ route.code }}</p>
              <p>Status: {{ route.status }}</p>
              <p v-if="route.stops.length">
                Average selling places:{{ route.places }}
              </p>
            </div>
          </div>
          <div class="buttons">
            <button
              class="delete"
              @click="deleteRoute((index = index), (code = route.code))"
            >
              <v-icon>mdi-delete</v-icon>
            </button>
          </div>
        </v-card>
      </li>
    </ul>
    <create-route-modal :open="open" />
    <update-route-modal :edit="edit" />
  </div>
</template>

<script>
import CreateRouteModal from "@/components/createRouteModal.vue";
import UpdateRouteModal from "@/components/updateRouteModal.vue";
// import updateTravelModal from '@/components/updateTravelModal.vue';
export default {
  components: { CreateRouteModal, UpdateRouteModal },
  data() {
    return {
      edit: false,
      open: false,
      routes: [],
    };
  },
  methods: {
    async getRoutes() {
      await fetch("http://127.0.0.1:8000/back/route", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          console.log("data =", data);
          return (this.routes = data);
        })
      );
    },
    async deleteRoute(index, code) {
      this.routes.splice(index, 1); //quita elemento de la data local
      await fetch(`http://127.0.0.1:8000/back/route?code=${code}`, {
        method: "DELETE",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) => res.json().then((data) => console.log(data)));
    },
  },
  created() {
    this.getRoutes();
  },
};
</script>

<style scoped>
.v-icon {
  color: #021c36;
}
.item {
  margin-left: 1rem;
}
.item_card {
  display: flex;
  justify-content: space-between;
  background-color: white;
}
.buttons {
  display: flex;
  align-items: center;
  padding-right: 1rem;
}
</style>