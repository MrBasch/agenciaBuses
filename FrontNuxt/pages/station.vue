<template>
  <div>
    <div class="header_">
      <h1>Station</h1>
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
      <li v-for="(station, index) in stations" :key="station.rut">
        <v-card height="5rem" class="item_card">
          <div class="item">
            <h1>Name: {{ station.name }}</h1>
            <div class="subtitle">
              <p>Code: {{ station.code }}</p>
              <p>City: {{ station.city.name }}</p>
            </div>
          </div>
          <div class="buttons">
            <button class="delete" @click="deleteStation(index, station.id)">
              <v-icon>mdi-delete</v-icon>
            </button>
          </div>
        </v-card>
      </li>
    </ul>
    <createStationModal :key="open" :open="open" />
    <updateStationModal :key="edit" :edit="edit" />
  </div>
</template>

<script>
import createStationModal from "@/components/createStationModal.vue";
import updateStationModal from "@/components/updateStationModal.vue";
export default {
  components: {
    createStationModal,
    updateStationModal,
  },
  data() {
    return {
      open: false,
      edit: false,
      stations: [],
    };
  },
  methods: {
    async deleteStation(index, id) {
      this.stations.splice(index, 1); //quita elemento de la data local
      await fetch(`http://127.0.0.1:8000/back/station?id=${id}`, {
        method: "DELETE",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) => res.json().then((data) => console.log(data)));
    },
    async getStations() {
      await fetch("http://127.0.0.1:8000/back/station", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          console.log("data =", data);
          this.stations = data;
        })
      );
    },
  },
  created() {
    this.getStations();
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