<template>
  <v-dialog max-width="500px" v-model="open">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Add Place</v-card-title>
      <v-form>
        <v-text-field v-model="code" label="Enter place code"></v-text-field>
        <v-select
          v-model="state"
          :items="status"
          label="is available?"
        ></v-select>
        <v-select
          v-model="selected_travel"
          :items="travels"
          label="Select a travel"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="savePlace(code, state, selected_travel)"
          color="#417D7A"
          >Add</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "createPlaceModal",
  props: ["open"],
  data() {
    return {
      code: "",
      state: "",
      status: ["True", "False"],
      selected_travel: "",
      travels: [],
    };
  },
  methods: {
    async savePlace(code, available, selected_travel) {
      await fetch(
        `http://127.0.0.1:8000/back/place?code=${code}&available=${available}&travel=${selected_travel}`,
        {
          method: "POST",
          mode: "cors",
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
          cache: "default",
        }
      ).then((res) => res.json().then((data) => console.log(data)));
    },
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
          data.map((travel) => this.travels.push(travel.code));
        })
      );
    },
  },
  created() {
    this.getTravels();
  },
};
</script>
<style scoped>
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
</style>