// DDC-CWICR-OE: DataDrivenConstruction · OpenConstructionERP
// Copyright (c) 2026 Artem Boiko / DataDrivenConstruction
/** Left-pane hierarchical folder and category tree for the file manager. */

import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import {
  FileText,
  Image as ImageIcon,
  Layout,
  Box,
  Pencil,
  Folder,
  FolderOpen,
  Tag,
  FileBarChart,
  PenTool,
  HardDrive,
  ChevronDown,
  ChevronRight,
  FolderTree as FolderTreeIcon,
} from 'lucide-react';
import clsx from 'clsx';
import type { FileTreeNode, FileKind } from '../types';
import { TrashNode } from '@/features/file-trash/TrashNode';
import { SavedViewsRail } from '@/features/file-saved-views';
import { fmtFixed } from '@/shared/lib/formatters';

const KIND_ICONS: Record<FileKind, typeof FileText> = {
  document: FileText,
  photo: ImageIcon,
  sheet: Layout,
  bim_model: Box,
  dwg_drawing: Pencil,
  takeoff: Tag,
  report: FileBarChart,
  markup: PenTool,
};

interface FileTreeProps {
  nodes: FileTreeNode[];
  selectedId: string | null;
  onSelect: (id: string | null) => void;
  isLoading?: boolean;
  projectId?: string | null;
}

function fmtBytes(bytes: number): string {
  if (!bytes) return '0 B';
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${fmtFixed(bytes / 1024, 1)} KB`;
  if (bytes < 1024 * 1024 * 1024) return `${fmtFixed(bytes / (1024 * 1024), 1)} MB`;
  return `${fmtFixed(bytes / (1024 * 1024 * 1024), 2)} GB`;
}

export function FileTree({ nodes, selectedId, onSelect, isLoading, projectId }: FileTreeProps) {
  const { t } = useTranslation();
  // State for expanded folders (default all top-level folders expanded)
  const [expandedIds, setExpandedIds] = useState<Set<string>>(() => {
    return new Set(nodes.filter((n) => n.children && n.children.length > 0).map((n) => n.id));
  });

  const isFolderTree = nodes.some((n) => n.kind === 'folder');
  const totalCount = nodes.reduce((acc, n) => acc + n.file_count, 0);
  const totalBytes = nodes.reduce((acc, n) => acc + n.total_bytes, 0);

  const toggleExpand = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setExpandedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  const STORAGE_TINTS: Record<FileKind, string> = {
    document: 'bg-blue-400',
    photo: 'bg-emerald-400',
    sheet: 'bg-amber-400',
    bim_model: 'bg-violet-400',
    dwg_drawing: 'bg-orange-400',
    takeoff: 'bg-cyan-400',
    report: 'bg-pink-400',
    markup: 'bg-rose-400',
  };

  const storageBreakdown = totalBytes > 0
    ? [...nodes]
        .filter((n) => n.total_bytes > 0)
        .sort((a, b) => b.total_bytes - a.total_bytes)
        .slice(0, 6)
    : [];

  return (
    <aside className="w-64 shrink-0 border-r border-border-light bg-surface-secondary/40 overflow-y-auto flex flex-col">
      {totalBytes > 0 && (
        <div className="px-3 pt-3 pb-3 border-b border-border-light shrink-0">
          <div className="flex items-center gap-1.5 mb-2 text-2xs font-medium uppercase tracking-wider text-content-tertiary">
            <HardDrive size={11} strokeWidth={2} />
            <span>{t('files.tree.storage_used', { defaultValue: 'Storage used' })}</span>
          </div>
          <div className="text-base font-semibold text-content-primary tabular-nums">
            {fmtBytes(totalBytes)}
          </div>
          <div className="text-[10px] text-content-tertiary mb-2">
            {totalCount} tập tin · {nodes.length} nhóm thư mục
          </div>
          <div
            className="flex h-1.5 w-full overflow-hidden rounded-full bg-surface-tertiary"
            role="img"
            aria-label={t('files.tree.storage_breakdown', { defaultValue: 'Storage by category' })}
          >
            {storageBreakdown.map((node, idx) => {
              const kind = node.id.replace(/^category:/, '') as FileKind;
              const pct = (node.total_bytes / totalBytes) * 100;
              const tint = STORAGE_TINTS[kind] ?? ['bg-blue-400', 'bg-amber-400', 'bg-emerald-400', 'bg-violet-400', 'bg-cyan-400'][idx % 5];
              return (
                <span
                  key={node.id}
                  className={clsx('block h-full', tint)}
                  style={{ width: `${pct}%` }}
                  title={`${node.label}: ${fmtBytes(node.total_bytes)}`}
                />
              );
            })}
          </div>
        </div>
      )}

      <div className="px-3 pt-3 pb-2 shrink-0">
        <div className="flex items-center justify-between text-2xs font-semibold uppercase tracking-wider text-content-tertiary px-1 mb-1.5">
          <span className="flex items-center gap-1.5">
            <FolderTreeIcon size={12} />
            {isFolderTree ? 'Cấu trúc thư mục dự án' : t('files.tree.title', { defaultValue: 'Categories' })}
          </span>
        </div>

        <button
          type="button"
          onClick={() => onSelect(null)}
          className={clsx(
            'w-full flex items-center gap-2 px-2 py-1.5 rounded-lg text-left text-xs transition-colors',
            selectedId === null
              ? 'bg-oe-blue/10 text-oe-blue font-semibold'
              : 'text-content-secondary hover:bg-surface-secondary',
          )}
        >
          <Folder size={14} className="shrink-0 text-oe-blue" />
          <span className="flex-1 truncate font-medium">
            {t('files.tree.all', { defaultValue: 'Tất cả tệp' })}
          </span>
          <span className="text-2xs text-content-tertiary tabular-nums bg-surface-tertiary px-1.5 py-0.5 rounded-full">
            {totalCount}
          </span>
        </button>
      </div>

      <div className="flex-1 px-2 pb-4 overflow-y-auto space-y-0.5">
        {nodes.map((node) => {
          if (node.kind === 'folder') {
            const hasChildren = node.children && node.children.length > 0;
            const isExpanded = expandedIds.has(node.id);
            const isSelected = selectedId === node.id;

            return (
              <div key={node.id} className="space-y-0.5">
                <div
                  onClick={() => onSelect(node.id)}
                  className={clsx(
                    'group flex items-center gap-1.5 px-2 py-1.5 rounded-lg text-left text-xs transition-colors cursor-pointer select-none',
                    isSelected
                      ? 'bg-oe-blue/10 text-oe-blue font-semibold'
                      : 'text-content-secondary hover:bg-surface-secondary hover:text-content-primary',
                  )}
                  title={node.label}
                >
                  {hasChildren ? (
                    <button
                      type="button"
                      onClick={(e) => toggleExpand(node.id, e)}
                      className="p-0.5 rounded hover:bg-black/5 dark:hover:bg-white/10 text-content-tertiary hover:text-content-primary transition-colors shrink-0"
                    >
                      {isExpanded ? <ChevronDown size={12} /> : <ChevronRight size={12} />}
                    </button>
                  ) : (
                    <span className="w-3 shrink-0" />
                  )}

                  {isExpanded || isSelected ? (
                    <FolderOpen size={14} className="shrink-0 text-amber-500" />
                  ) : (
                    <Folder size={14} className="shrink-0 text-amber-500/80" />
                  )}

                  <span className="flex-1 truncate font-medium text-xs leading-tight">
                    {node.label}
                  </span>

                  <span
                    className={clsx(
                      'text-[10px] tabular-nums px-1.5 py-0.2 rounded-full shrink-0',
                      node.file_count > 0
                        ? 'bg-oe-blue/10 text-oe-blue font-medium'
                        : 'text-content-quaternary',
                    )}
                  >
                    {node.file_count}
                  </span>
                </div>

                {/* Subfolders */}
                {hasChildren && isExpanded && (
                  <div className="ml-4 pl-2 border-l border-border-light/60 space-y-0.5">
                    {node.children.map((child) => {
                      const childSelected = selectedId === child.id;
                      return (
                        <div
                          key={child.id}
                          onClick={() => onSelect(child.id)}
                          className={clsx(
                            'flex items-center gap-1.5 px-2 py-1 rounded-md text-left text-xs transition-colors cursor-pointer select-none',
                            childSelected
                              ? 'bg-oe-blue/10 text-oe-blue font-semibold'
                              : 'text-content-tertiary hover:bg-surface-secondary hover:text-content-primary',
                          )}
                          title={child.label}
                        >
                          <Folder size={12} className="shrink-0 text-amber-400" />
                          <span className="flex-1 truncate text-2xs leading-tight">
                            {child.label}
                          </span>
                          <span
                            className={clsx(
                              'text-[9px] tabular-nums px-1 rounded shrink-0',
                              child.file_count > 0
                                ? 'bg-surface-tertiary text-content-secondary font-medium'
                                : 'text-content-quaternary',
                            )}
                          >
                            {child.file_count}
                          </span>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          }

          // Fallback legacy FileKind node
          const kind = node.id.replace(/^category:/, '') as FileKind;
          const Icon = KIND_ICONS[kind] ?? Folder;
          const isActive = selectedId === kind;
          return (
            <div key={node.id}>
              <button
                type="button"
                onClick={() => onSelect(kind)}
                className={clsx(
                  'w-full flex items-center gap-2 px-2 py-1.5 rounded-lg text-left text-xs transition-colors',
                  isActive
                    ? 'bg-oe-blue/10 text-oe-blue font-semibold'
                    : 'text-content-secondary hover:bg-surface-secondary',
                )}
              >
                <Icon size={14} className="shrink-0" />
                <span className="flex-1 truncate">
                  {t(`files.category.${kind}`, { defaultValue: node.label })}
                </span>
                <span className="text-2xs text-content-tertiary tabular-nums shrink-0">
                  {node.file_count}
                </span>
              </button>
            </div>
          );
        })}

        {!isLoading && nodes.length === 0 && (
          <div className="px-2 py-3 text-xs text-content-tertiary text-center">
            {t('files.tree.empty', { defaultValue: 'Chưa có tệp nào' })}
          </div>
        )}
      </div>

      {projectId && (
        <div className="border-t border-border-light pt-2 mt-auto shrink-0">
          <SavedViewsRail projectId={projectId} />
        </div>
      )}

      <div className="px-3 pb-3 border-t border-border-light pt-2 shrink-0">
        <TrashNode projectId={projectId ?? null} active={selectedId === 'trash'} />
      </div>
    </aside>
  );
}
