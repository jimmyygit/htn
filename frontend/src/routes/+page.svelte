<script lang="ts">
	import Button from '@smui/button';
	import Textfield from '@smui/textfield';
	import Fab, { Icon } from '@smui/fab';

	let valueA = '';
</script>

<div class="relative h-full">
	<Textfield
		style="width: 500px"
		class="shaped-filled"
		variant="filled"
		bind:value={valueA}
		label="Note"
	/>

	<Button on:click={() => alert(valueA)} color="primary">Add Note</Button>

	<Fab
		on:click={() => console.log('create item')}
		class="flex absolute left-1/2 -translate-x-1/2 bottom-4"
		color="primary"
	>
		<Icon class="material-icons">add</Icon>
	</Fab>
</div>
