<script lang="ts">
import { Content, Header, Panel } from '@smui-extra/accordion';
import IconButton, { Icon } from '@smui/icon-button';
import List, { Item, Meta, Label } from '@smui/list';
import Checkbox from '@smui/checkbox';
import { createEventDispatcher } from 'svelte';
import Dialog, { Title, Content as DiaContent, Actions } from '@smui/dialog';


const dispatch = createEventDispatcher()

export let label: string;
export let open: boolean = false;
export let content: any[] = [];
export let suggestion: string;
let modalOpen = false;


export let activeTab: string;
interface CheckBoxStates {
    [key: string]: boolean;
}
export let checkBoxStates: CheckBoxStates;

function handleClick() {
	dispatch('itemChanged');
}

</script>

<Panel bind:open variant="unelevated">
<Header>
	{label}
	<IconButton slot="icon" toggle pressed={open}>
		<Icon class="material-icons" on>expand_less</Icon>
		<Icon class="material-icons">expand_more</Icon>
	</IconButton>
</Header>
<Content>
	{#if content.length == 0}
	<div class="text-sm text-gray-500"> No sub tasks </div>
{/if}

<!-- <Dialog
  bind:modalOpen
  aria-labelledby="simple-title"
  aria-describedby="simple-content"
>
  <Title id="simple-title">Suggestion</Title>
  <DiaContent id="simple-content">Super awesome dialog body text?</DiaContent>
</Dialog> -->

<List>
	{#each content as item}
	<Item class="flex justify-between">
		<Label>{item}</Label>
			<button on:click={() => (modalOpen = true)}>
				<span class="material-icons">settings_suggest</span>
			</button>
	</Item>
	{/each}
	</List>
</Content>
</Panel>




