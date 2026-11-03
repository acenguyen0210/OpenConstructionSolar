// DDC-CWICR-OE: DataDrivenConstruction · OpenConstructionERP
// Copyright (c) 2026 Artem Boiko / DataDrivenConstruction
// FilesStatsStrip — landing-view KPI strip + storage-by-folder/category breakdown.

import type { ReactNode } from 'react';
import { useMemo } from 'react';
import { useTranslation } from 'react-i18next';
import { Database, FileText, HardDrive, Layers } from 'lucide-react';
import type { FileKind, FileTreeNode, StorageLocations } from '../types';
import { ALL_KINDS, KIND_COLORS } from '../kindModule';
import { fmtPercent, fmtFixed } from '@/shared/lib/formatters';
import { getNumberLocale } from '@/stores/usePreferencesStore';

const FOLDER_TINTS = [
  'bg-blue-500',
  'bg-amber-500',
  'bg-emerald-500',
  'bg-purple-500',
  'bg-rose-500',
  'bg-cyan-500',
  'bg-indigo-500',
  'bg-teal-500',
  'bg-orange-500',
  'bg-pink-500',
  'bg-lime-500',
  'bg-violet-500',
];

function fmtBytes(bytes: number): string {
  if (bytes === 0 || !Number.isFinite(bytes)) return '0 B';
  const units = ['B', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.floor(Math.log(bytes) / Math.log(1024));
  const v = bytes / Math.pow(1024, i);
  return `${fmtFixed(v, v >= 100 || i === 0 ? 0 : 1)} ${units[i] ?? 'TB'}`;
}

interface FilesStatsStripProps {
  tree: FileTreeNode[] | undefined;
  locations: StorageLocations | undefined;
}

export function FilesStatsStrip({ tree, locations }: FilesStatsStripProps) {
  const { t } = useTranslation();

  const stats = useMemo(() => {
    if (!tree || tree.length === 0) return null;
    const isFolder = tree.some((n) => n.kind === 'folder');
    const totalFiles = tree.reduce((s, n) => s + n.file_count, 0);
    const totalBytes = tree.reduce((s, n) => s + n.total_bytes, 0);
    const populated = tree.filter((n) => n.file_count > 0).length;
    const segments = tree
      .filter((n) => n.total_bytes > 0)
      .map((n, idx) => ({
        id: n.id,
        label: n.label,
        bytes: n.total_bytes,
        pct: totalBytes > 0 ? (n.total_bytes / totalBytes) * 100 : 0,
        color: isFolder
          ? FOLDER_TINTS[idx % FOLDER_TINTS.length]
          : KIND_COLORS[n.id as FileKind] ?? 'bg-gray-400',
      }))
      .sort((a, b) => b.bytes - a.bytes);
    return { totalFiles, totalBytes, populated, segments, isFolder };
  }, [tree]);

  if (!stats || stats.totalFiles === 0) return null;

  const backendRaw = locations?.storage_backend ?? '';
  const backendLabel = backendRaw === 's3'
    ? t('files.stats_backend_s3', { defaultValue: 'S3-compatible' })
    : backendRaw === 'local'
      ? t('files.stats_backend_local', { defaultValue: 'Đĩa cục bộ' })
      : '—';

  return (
    <div className="border-b border-border-light bg-surface-elevated/60">
      {/* KPI row */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 px-4 py-3">
        <Metric
          icon={<FileText size={14} />}
          label={t('files.stats_total', { defaultValue: 'Tổng số tập tin' })}
          value={stats.totalFiles.toLocaleString(getNumberLocale())}
        />
        <Metric
          icon={<HardDrive size={14} />}
          label={t('files.stats_size', { defaultValue: 'Tổng kích thước' })}
          value={fmtBytes(stats.totalBytes)}
        />
        <Metric
          icon={<Layers size={14} />}
          label={stats.isFolder ? 'Thư mục dự án' : t('files.stats_categories', { defaultValue: 'Danh mục' })}
          value={stats.isFolder ? `${tree?.length ?? 12} nhóm thư mục` : `${stats.populated} / ${ALL_KINDS.length}`}
        />
        <Metric
          icon={<Database size={14} />}
          label={t('files.stats_backend', { defaultValue: 'Bộ nhớ' })}
          value={backendLabel}
        />
      </div>

      {/* Storage breakdown bar */}
      {stats.segments.length > 0 && (
        <div className="px-4 pb-3">
          <div className="flex items-center justify-between gap-2 mb-1.5">
            <div className="text-2xs font-medium text-content-tertiary uppercase tracking-wider">
              {stats.isFolder ? 'Dung lượng theo nhóm hồ sơ' : t('files.stats_breakdown', { defaultValue: 'Storage by category' })}
            </div>
            <div className="text-2xs text-content-quaternary tabular-nums">
              {fmtBytes(stats.totalBytes)}
            </div>
          </div>
          <div
            className="flex h-2 rounded-full overflow-hidden bg-surface-tertiary"
            role="img"
          >
            {stats.segments.map((seg) => (
              <span
                key={seg.id}
                className={seg.color}
                style={{ width: `${seg.pct}%` }}
                title={`${seg.label}: ${fmtBytes(seg.bytes)} (${fmtPercent(seg.pct, 1)})`}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

interface MetricProps {
  icon: ReactNode;
  label: string;
  value: string;
}

function Metric({ icon, label, value }: MetricProps) {
  return (
    <div className="flex items-center gap-2.5 p-2 rounded-lg bg-surface-primary/40 border border-border-light/60">
      <span className="flex h-7 w-7 items-center justify-center rounded-md bg-surface-secondary text-content-secondary shrink-0">
        {icon}
      </span>
      <div className="min-w-0">
        <div className="text-2xs text-content-tertiary truncate uppercase tracking-wider font-medium">
          {label}
        </div>
        <div className="text-sm font-semibold text-content-primary truncate tabular-nums">
          {value}
        </div>
      </div>
    </div>
  );
}
