'use client';

import { Filter } from 'lucide-react';

interface DivisionOption {
  division: string;
  count: number;
}

interface DivisionFilterBarProps {
  selectedDivision: string;
  onSelectDivision: (division: string) => void;
  divisions: DivisionOption[];
}

// Clean readable department abbreviations / labels
function formatDivisionName(name: string): string {
  return name
    .replace('Division', '')
    .replace('and Information Technology', '& IT')
    .replace('and Hospital Planning', '')
    .trim();
}

export default function DivisionFilterBar({
  selectedDivision,
  onSelectDivision,
  divisions,
}: DivisionFilterBarProps) {
  if (!divisions || divisions.length === 0) return null;

  const totalCount = divisions.reduce((acc, curr) => acc + curr.count, 0);

  return (
    <div className="w-full my-3">
      <div className="flex items-center gap-1.5 mb-2 px-1">
        <Filter size={12} className="text-slate-500 dark:text-slate-400" />
        <span className="text-[11px] font-semibold text-slate-600 dark:text-slate-400 uppercase tracking-wider">
          Filter by Technical Department
        </span>
      </div>

      <div className="flex items-center gap-1.5 overflow-x-auto custom-scrollbar pb-1.5">
        {/* All option */}
        <button
          onClick={() => onSelectDivision('All')}
          className={`
            shrink-0 px-2.5 py-1 rounded-lg text-[11px] font-medium transition-all duration-150 flex items-center gap-1.5 border
            ${
              selectedDivision === 'All'
                ? 'bg-slate-900 text-white border-slate-900 dark:bg-white dark:text-black dark:border-white shadow-xs'
                : 'bg-white dark:bg-black text-slate-700 dark:text-neutral-300 border-slate-300 dark:border-neutral-800 hover:border-slate-500 dark:hover:border-neutral-700 hover:bg-slate-50 dark:hover:bg-neutral-900'
            }
          `}
        >
          <span>All Departments</span>
          <span
            className={`text-[9.5px] px-1.5 py-0.2 rounded-md font-semibold ${
              selectedDivision === 'All'
                ? 'bg-slate-700 text-slate-100 dark:bg-neutral-200 dark:text-black'
                : 'bg-slate-100 dark:bg-neutral-900 text-slate-600 dark:text-neutral-400'
            }`}
          >
            {totalCount}
          </span>
        </button>

        {/* Individual Divisions */}
        {divisions.map((div) => {
          const isSelected = selectedDivision === div.division;
          return (
            <button
              key={div.division}
              onClick={() => onSelectDivision(div.division)}
              className={`
                shrink-0 px-2.5 py-1 rounded-lg text-[11px] font-medium transition-all duration-150 flex items-center gap-1.5 border
                ${
                  isSelected
                    ? 'bg-blue-600 text-white border-blue-600 shadow-xs'
                    : 'bg-white dark:bg-black text-slate-700 dark:text-neutral-300 border-slate-300 dark:border-neutral-800 hover:border-slate-500 dark:hover:border-neutral-700 hover:bg-slate-50 dark:hover:bg-neutral-900'
                }
              `}
              title={div.division}
            >
              <span>{formatDivisionName(div.division)}</span>
              <span
                className={`text-[9.5px] px-1.5 py-0.2 rounded-md font-semibold ${
                  isSelected
                    ? 'bg-blue-700 text-white'
                    : 'bg-slate-100 dark:bg-neutral-900 text-slate-600 dark:text-neutral-400'
                }`}
              >
                {div.count}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
