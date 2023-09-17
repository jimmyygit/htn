<script lang="ts">
import { Content, Header, Panel } from '@smui-extra/accordion';
import IconButton, { Icon } from '@smui/icon-button';
import List, { Item, Meta, Label } from '@smui/list';
import Checkbox from '@smui/checkbox';
import { createEventDispatcher } from 'svelte';

const dispatch = createEventDispatcher()

export let label: string;
export let open: boolean = false;
export let content: any[] = [];

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
	{#if activeTab === "Notes"}
	<List
class="demo-list"
checkList

> {#each content as item}
	<Item>
		<Label>{item}</Label>
		<Meta>
			<button>
				<span class="material-icons">delete</span>
			</button>

		</Meta>
		
		
	</Item>
	{/each}
	</List>
	{:else}
	<List class="demo-list" checkList> 
	{#each content as item}
	<Item>
		<Label>{item}</Label>
		<Meta>
			<Checkbox bind:checked={checkBoxStates[item]} on:change(e)={handleClick} />
			</Meta>
	</Item>
	{/each}
	</List>
	{/if}
</Content>
</Panel>




