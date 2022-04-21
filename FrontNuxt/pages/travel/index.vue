<template>
  <div>
    <div class="header_">
      <h1>Travels</h1>
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
      <li v-for="(travel, index) in travels" :key="travel.code">
        <v-card height="5rem" class="item_card">
          <div class="item">
            <h1>Travel code: {{ travel.code }}</h1>
            <div class="subtitle">
              <p>Code: {{ travel.code }}</p>
              <p>Start time: {{ travel.start_time }}</p>
              <p>End time: {{ travel.end_time }}</p>
            </div>
          </div>
          <div class="buttons">
            <button
              class="delete"
              @click="deleteTravel((index = index), (code = travel.code))"
            >
              <v-icon>mdi-delete</v-icon>
            </button>
          </div>
        </v-card>
      </li>
    </ul>
    <create-travel-modal :open="open" />
    <update-travel-modal :edit="edit" />
  </div>
</template>

<script>
import createTravelModal from "@/components/createTravelModal.vue";
import updateTravelModal from "@/components/updateTravelModal.vue";
export default {
  components: { createTravelModal, updateTravelModal },
  data() {
    return {
      edit: false,
      open: false,
      travels: [],
    };
  },
  methods: {
    async getTravels() {
      await fetch("http://127.0.0.1:8000/back/travel", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          this.travels = data;
        })
      );
    },
    async deleteTravel(index, code) {
      this.travels.splice(index, 1); //quita elemento de la data local
      await fetch(`http://127.0.0.1:8000/back/travel?code=${code}`, {
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
    this.getTravels();
  },
};
</script>

<style scoped>
ul {
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.subtitle {
  display: flex;
  gap: 0.8rem;
}
h1,
p,
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