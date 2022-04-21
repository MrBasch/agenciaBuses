<template>
  <div>
    <div class="header_">
      <h1>Passenger</h1>
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
      <li v-for="(passenger, index) in passengers" :key="passenger.rut">
        <v-card height="5rem" class="item_card">
          <div class="item">
            <h1>Name: {{ passenger.name }}</h1>
            <div class="subtitle">
              <p>Rut: {{ passenger.rut }}</p>
            </div>
          </div>
          <div class="buttons">
            <button class="delete" @click="deletePassenger((index = index))">
              <v-icon>mdi-delete</v-icon>
            </button>
          </div>
        </v-card>
      </li>
    </ul>
    <createPassengerModal :key="open" :open="open" />
    <updatePassengerModal :key="edit" :edit="edit" />
  </div>
</template>

<script>
import createPassengerModal from "@/components/createPassengerModal.vue";
import updatePassengerModal from "@/components/updatePassengerModal.vue";
// import updateBusModal from '@/components/updateBusModal.vue';
export default {
  components: {
    createPassengerModal,
    updatePassengerModal,
  },
  data() {
    return {
      open: false,
      edit: false,
      passengers: [],
    };
  },
  methods: {
    async deletePassenger(index) {
      this.passengers.splice(index, 1); //quita elemento de la data local
      await fetch(`http://127.0.0.1:8000/back/passenger?id=${index}`, {
        method: "DELETE",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) => res.json().then((data) => console.log(data)));
    },
    async getPassengers() {
      await fetch("http://127.0.0.1:8000/back/passenger", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          console.log("data =", data);
          return (this.passengers = data);
        })
      );
    },
  },
  created() {
    this.getPassengers();
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