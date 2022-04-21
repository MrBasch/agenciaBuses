<template>
  <div>
    <div class="header_">
      <h1>Place</h1>
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
      <li v-for="(place, index) in places" :key="place.code">
        <v-card height="5rem" class="item_card">
          <div class="item">
            <h1>Code: {{ place.code }}</h1>
            <div class="subtitle">
              <p>travel code: {{ place.travel.code }}</p>
              <p v-if="place.available">Status: Available</p>
              <p v-else>Status: No Available</p>
            </div>
          </div>
          <div class="buttons">
            <button class="delete" @click="deletePlace(index, place.code)">
              <v-icon>mdi-delete</v-icon>
            </button>
          </div>
        </v-card>
      </li>
    </ul>
    <createPlaceModal :key="open" :open="open" />
    <updatePlaceModal :key="edit" :edit="edit" />
  </div>
</template>

<script>
import createPlaceModal from "@/components/createPlaceModal.vue";
import updatePlaceModal from "@/components/updatePlaceModal.vue";
export default {
  components: {
    createPlaceModal,
    updatePlaceModal,
  },
  data() {
    return {
      open: false,
      edit: false,
      places: [],
    };
  },
  methods: {
    async deletePlace(index, code) {
      this.places.splice(index, 1); //quita elemento de la data local
      await fetch(`http://127.0.0.1:8000/back/place?code=${code}`, {
        method: "DELETE",
        mode: "cors",
        headers: {
          Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
        },
        cache: "default",
      }).then((res) => res.json().then((data) => console.log(data)));
    },
    async getPlaces() {
      await fetch("http://127.0.0.1:8000/back/place", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          console.log("data =", data);
          return (this.places = data);
        })
      );
    },
  },
  created() {
    this.getPlaces();
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