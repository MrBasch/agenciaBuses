<template>
  <div>
    <div class="header_">
      <h1>City</h1>
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
      <li v-for="(city, index) in cities" :key="city.code">
        <v-card height="5rem" class="item_card">
          <div class="item">
            <h1>Name: {{ city.name }}</h1>
            <div class="subtitle">
              <p>Code: {{ city.code }}</p>
            </div>
          </div>
          <div class="buttons">
            <button class="delete" @click="deleteCity(index, city.code)">
              <v-icon>mdi-delete</v-icon>
            </button>
          </div>
        </v-card>
      </li>
    </ul>
    <createCityModal :key="open" :open="open" />
    <updateCityModal :key="edit" :edit="edit" />
  </div>
</template>

<script>
import createCityModal from "@/components/createCityModal.vue";
import updateCityModal from "@/components/updateCityModal.vue";
export default {
  components: {
    createCityModal,
    updateCityModal,
  },
  data() {
    return {
      open: false,
      edit: false,
      cities: [],
    };
  },
  methods: {
    async deleteCity(index, code) {
      this.cities.splice(index, 1); //quita elemento de la data local
      await fetch(`http://127.0.0.1:8000/back/city?code=${code}`, {
        method: "DELETE",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) => res.json().then((data) => console.log(data)));
    },
    async getCities() {
      await fetch("http://127.0.0.1:8000/back/city", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          console.log("data =", data);
          return (this.cities = data);
        })
      );
    },
  },
  created() {
    this.getCities();
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