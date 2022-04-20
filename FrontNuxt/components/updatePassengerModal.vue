<template>
  <v-dialog max-width="500px" v-model="edit">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create Passenger</v-card-title>
      <v-form>
        <v-text-field
          v-model="name"
          label="Enter passenger name"
        ></v-text-field>
        <v-text-field v-model="rut" label="Enter passenger rut"></v-text-field>
        <v-text-field
          v-model="new_rut"
          label="Enter new - passenger rut"
        ></v-text-field>
        <v-select
          v-model="place"
          :items="places"
          label="Select a place"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="
            updatePassenger(
              (place = place),
              (name = name),
              (rut = rut),
              (new_rut = new_rut)
            )
          "
          color="#417D7A"
          >Add</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "updatePassengerModal",
  props: ["edit"],
  data() {
    return {
      name: "",
      rut: "",
      new_rut: "",
      place: "",
      places: [],
    };
  },
  methods: {
    async updatePassenger(place, name, rut, new_rut) {
      console.log("place", place, "name", name, "rut", rut, "new_rut", new_rut);
      await fetch(
        `http://127.0.0.1:8000/back/passenger?place=${place}&name=${name}&rut=${rut}&new_rut=${new_rut}`,
        {
          method: "PUT",
          mode: "cors",
          headers: {
            Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
          },
          cache: "default",
        }
      ).then((res) => res.json().then((data) => console.log(data)));
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
          data.map((place) => this.places.push(place.code));
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
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
.cardTitle {
  background-color: #1a3c40;
}
</style>