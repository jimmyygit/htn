<script lang="ts">
	import Tab, { Label } from '@smui/tab';
	import TabBar from '@smui/tab-bar';
	import Accordion from '@smui-extra/accordion';
	import Button from '@smui/button';
	import { Input } from '@smui/textfield';
	import SubcategoryPanel from '$lib/components/SubcategoryPanel.svelte';

	interface Subcategory {
		[key: string]: { content: string[]; open: boolean };
	}

	let categories: { [key: string]: Subcategory } = {
		Tasks: {
			Shopping: { content: ['eggs', 'tomatoes'], open: false },
			Homework: { content: ['eggs', 'tomatoes'], open: false },
			General: { content: ['eggs', 'tomatoes'], open: false }
		},
		Goals: {
			Personal: { content: ['eggs', 'tomatoes'], open: false },
			Career: { content: ['eggs', 'tomatoes'], open: false }
		},
		Notes: {
			Ideas: { content: ['eggs', 'tomatoes'], open: false },
			'For later': { content: ['eggs', 'tomatoes'], open: false }
		}
	};
	let tabs = Object.keys(categories);
	let activeTab = tabs[0];

	let note = '';
	function submitNote() {
		const condensedCategories = [];
		for (const category of Object.keys(categories)) {
			for (const subcategory of Object.keys(categories[category])) {
				condensedCategories.push(`${subcategory}_${category}`);
			}
		}

		// Perform API request and get category
		const result = 'Tasks_Homework';

		// Split result
		const [categoryResult, subcategoryResult] = result.split('_');

		// Animate adding note
		activeTab = categoryResult;

		setTimeout(() => {
			categories[categoryResult][subcategoryResult].open = true;
			setTimeout(() => {
				categories[categoryResult][subcategoryResult].content = [
					...categories[categoryResult][subcategoryResult].content,
					note
				];
				note = '';
			}, 300);
		}, 100);
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
			{#each Object.keys(categories[activeTab]) as subcategoryName}
				<SubcategoryPanel
					label={subcategoryName}
					content={categories[activeTab][subcategoryName].content}
					open={categories[activeTab][subcategoryName].open}
				/>
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
