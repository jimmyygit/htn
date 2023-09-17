<script lang="ts">
	import Tab, { Label } from '@smui/tab';
	import TabBar from '@smui/tab-bar';
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import IconButton, { Icon } from '@smui/icon-button';
	import Button from '@smui/button';
	import { Input } from '@smui/textfield';
	import SubcategoryPanel from '$lib/components/SubcategoryPanel.svelte';

	interface Subcategory {
		[key: string]: { content: string[]; open: boolean };
	}

	let categories: { [key: string]: Subcategory } = {
		Tasks: {
			Shopping: { content: ['ones', 'two'], open: false },
			Homework: { content: ['three', 'four'], open: false },
			General: { content: ['five', 'six'], open: false }
		},
		Goals: {
			Personal: { content: ['seven', 'eigh'], open: false },
			Career: { content: ['nine', '10'], open: false }
		},
		Notes: {
			Ideas: { content: ['11', '12'], open: false },
			'For later': { content: ['13', '14'], open: false }
		}
	};
	let tabs = Object.keys(categories);
	let activeTab = tabs[0];
	let note = '';
	function submitNote() {}

  interface CheckBoxStates {
    [key: string]: boolean;
}

const checkBoxStates: CheckBoxStates = {};

Object.entries(categories).forEach(([categoryName, subcategories]) => {
    Object.entries(subcategories).forEach(([subcategoryName, subcategory]) => {
        subcategory.content.forEach(item => {
            const uniqueKey = `${categoryName}_${subcategoryName}_${item}`;
            checkBoxStates[uniqueKey] = false;
        });
    });
});

function handleCheckChange(e: CustomEvent) {
    const isChecked = (e.target as HTMLInputElement).checked;
    const category = e.detail.category;
    const subcategory = e.detail.subcategory;
    const item = e.detail.item;
    const uniqueKey = `${category}_${subcategory}_${item}`;
    checkBoxStates[uniqueKey] = isChecked;
    localStorage.setItem(uniqueKey, isChecked.toString());
    
}

</script>

<div class="flex flex-col relative h-full">
	<div class="drop-shadow-md mb-2">
		<div class="bg-white py-2 w-full flex items-center justify-center">
			<img src="/logo.png" alt="Logo" style="height: 50px" />
		</div>
		<TabBar class="bg-white" tabs={['Tasks', 'Goals', 'Notes']} let:tab bind:active={activeTab}>
			<Tab {tab}>
				<Label>{tab}</Label>
			</Tab>
		</TabBar>
	</div>
	<div class="accordion-container">
		<Accordion>
			{#each Object.keys(categories[activeTab]) as subcategoryName (subcategoryName)}
				<SubcategoryPanel
					label={subcategoryName}
					content={categories[activeTab][subcategoryName].content}
					open={categories[activeTab][subcategoryName].open}
          activeTab={activeTab}
          checkBoxStates={checkBoxStates}
           
     
        
          on:itemChanged={handleCheckChange} />
				
			{/each}
		</Accordion>
	</div>

	<div class="flex-1" />

	<div class="p-4 flex items-baseline gap-2 bg-gray-100">
		<Input bind:value={note} class="solo-input" placeholder="Jot something down..." autofocus />
		<Button disabled={note.length === 0} on:click={submitNote}>Submit</Button>
	</div>
</div>

<style>
	* :global(.solo-input::placeholder) {
		color: var(--mdc-theme-on-surface, #000);
		opacity: 0.6;
	}
</style>
